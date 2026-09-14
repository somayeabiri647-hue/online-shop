from sqlalchemy import *
from extention import db
import models.user

class Cart(db.Model):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key = True)
    status = Column(String, default="pending")
    user_id = Column(Integer , ForeignKey("users.id"), nallable = False )
    user = db.relationship("User" , backref = "carts")