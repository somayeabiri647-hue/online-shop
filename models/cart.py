from sqlalchemy import *
from extention import db
from sqlalchemy.orm import backref
import models.user


class Cart(db.Model):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key = True)
    status = Column(String, default="pending")
    user_id = Column(Integer , ForeignKey("user.id"), nullable = False )
    user = db.relationship("User" , backref = backref ( "carts" , lazy = "dynamic"))