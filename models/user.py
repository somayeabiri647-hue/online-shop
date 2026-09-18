from sqlalchemy import Column, Integer, String
from extention import db , get_current_time
from flask_login import UserMixin
import extention
class User(db.Model , UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, index=True)
    password = Column(String, nullable=False)
    phone = Column(String(11) , nullable=False , index=True)
    address = Column(String, nullable=False, index=True)
    date_created = Column(String(15) ,default = get_current_time )