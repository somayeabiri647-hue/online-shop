from sqlalchemy import Column, Integer, String
import extention
from flask_login import UserMixin
db = extention.db

class User(db.Model , UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, index=True)
    password = Column(String, nullable=False)
    phone = Column(String(11) , nullable=False , index=True)
    address = Column(String, nullable=False, index=True)