from sqlalchemy import Column, Integer, String
import extention

db = extention.db

class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, index=True)
    password = Column(String, nullable=False)
    address = Column(String, nullable=False, index=True)