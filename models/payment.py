from sqlalchemy import *
from extention import db
import models.user

class payment(db.Model):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key = True)
    status = Column(String, default="pending")
    cart_id = Column(Integer , ForeignKey("carts.id"), nallable = False )
    cart = db.relationship("Cart" , backref = "payments")