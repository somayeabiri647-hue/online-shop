from sqlalchemy import *
from extention import db
import models.user

class product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key = True)
    name = Column(String, unique = True, nullable = False, index = True)
    description = Column(String(11), nullable = False, index = True)
    price = Column(Integer, nullable = False, index = True)
    active = Column(Integer, nullable = False, index = True)
