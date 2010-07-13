"""Namespace model"""
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String, Text

from wikpy.model.meta import Base

class Namespace(Base):
	__tablename__ = "namespaces"
	
	id = Column(Integer, primary_key=True)
	name = Column(String(100))
	pages = relationship('Page')
	
	def __init__(self, name=''):
		self.name = name
		
	def __repr__(self):
		return "<Namespace('%s')" % self.name