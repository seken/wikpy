import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
import wikpy.lib.helpers as help
from pylons.decorators.cache import beaker_cache

from pylons import cache, request
from pylons.decorators.cache import create_cache_key

import markdown2

from webhelpers.html import escape

from wikpy.lib.base import BaseController, render, Session

from wikpy.model.page import Page
from wikpy.model.namespace import Namespace
from wikpy.model.tag import Tag

log = logging.getLogger(__name__)

class EmptyPage:
	def __init__(self, name, blank=False):
		self.name = name
		self.namespace = 'None'
		if blank:
			self.text = ''
		else:
			self.text = '''This page does not exist, click [here](/edit/%s) to create it.''' % escape(name)
		self.tags = []

class PageController(BaseController):
	
	def __before__(self):
		self.page_query = Session.query(Page)

	#@beaker_cache(expire=600, type='memory', query_args=True)
	def show(self, page):
		c.page = self._fetchPage(page)
		if c.page == None:
			c.page = EmptyPage(page)
		c.links = [('edit/%s' % page, 'edit')]
		c.text = help.literal(markdown2.markdown(c.page.text))
		return render('page.mako')
		
	def edit(self, page):
		c.page = self._fetchPage(page)
		if c.page == None:
			c.page = EmptyPage(page, True)
		c.links = []
		return render('edit.mako')
		
	def save(self, page):
		namespace, key = create_cache_key(self.show, {'page':page,})
		cache.get_cache(namespace).remove(key)
		np = self._splitName(page)
		newPage = self._fetchPage(page)
		if newPage == None:
			newPage = Page(np[1])
			newPage.namespace = Namespace(np[0])
			Session.add(newPage)
		newPage.text = request.POST['text']
		tags = list()
		for i in request.POST['tags'].split(','):
			if len(i) > 0:
				tags.append(Tag(i))
		Session.commit()
		redirect('/%s' % page)
		
	def _fetchPage(self, page):
		np = self._splitName(page)
		# TODO return namespace pages
		query = self.page_query.join(Namespace).filter(Page.name == np[1]).filter(Namespace.name == np[0])
		try:
			return query.one()
		except:
			return None
					
	def _splitName(self, page):
		np = page.split('::')
		if len(np) == 1:
			np = ['None'] + np
		return np