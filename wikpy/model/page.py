"""Page model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String, Text

from wikpy.model.meta import Base
from wikpy.model.tag import Tag, TagJoin
from wikpy.model.namespace import Namespace

class Page(Base):
	__tablename__ = "pages"

	id = Column(Integer, primary_key=True)
	name = Column(String(100))
	namespace_id = Column(Integer, ForeignKey('namespaces.id'))
	namespace = relationship(Namespace, primaryjoin=namespace_id == Namespace.id)
	tags = relationship(Tag, secondary=TagJoin)
	text = Column(Text())

	def __init__(self, name=''):
		self.name = name
		
	def __repr__(self):
		return "<Page('%s')" % self.name
		
	def fullname(self):
		if self.namespace.name != 'None':
			if self.name == '::' or len(self.name) == 0:
				return '%s::' % self.namespace.name
			else:
				return '%s::%s' % (self.namespace.name, self.name)
		else:
			return '%s' % self.name