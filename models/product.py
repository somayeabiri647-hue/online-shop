from sqlalchemy import *
from extention import db
import models.user

class product(db.Model):
    __tablname__ = 'product'
    id = column(Integer, primary_key = True)
    name = column(String, unique = True, nullable = False, index = True)
    description = column(String(11), nullable = False, index = True)
    price = column(Integer, nullable = False, index = True)
