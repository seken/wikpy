"""Tag model"""
from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.types import Integer, String, Text

from wikpy.model.meta import Base

TagJoin = Table(
	'tag2pageJoin', Base.metadata,
	Column('page_id', Integer, ForeignKey('pages.id')),
	Column('tag_id', Integer, ForeignKey('tags.id'))
	)

class Tag(Base):
	__tablename__ = "tags"
	
	id = Column(Integer, primary_key=True)
	name = Column(String(100))
	
	def __init__(self, name=''):
		self.name = name
		
	def __repr__(self):
		return "<Tag('%s')" % self.name