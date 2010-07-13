"""The application's model objects"""
from wikpy.model.meta import Session, Base

from wikpy.model.page import Page, Tag, Namespace

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
