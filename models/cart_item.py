from sqlalchemy import *
from extention import db
import models.user

class CartItem(db.Model):
    __tablename__ = 'cart_items'
    id = Column(Integer, primary_key = True)
    product_id = Column(Integer , ForeignKey("product.id"), nullable = False )
    cart_id = Column(Integer , ForeignKey("carts.id"), nullable = False )
    quantity =Column(Integer)

    product = db.relationship("product" , backref = "cart_items")
    cart = db.relationship("Cart" , backref = "cart_items")