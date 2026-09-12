from sqlalchemy import *
from extention import db
import models.user

class User(db.Model):
    __tablname__ = 'users'
    id = column(Integer, primary_key = True)
    username = column(String, unique = True, nullable = False, index = True)
    password = column(String, nullable = False, index = True)
    phone = column(String(11), nullable = False, index = True)
    address = column(String, nullable = False, index = True)