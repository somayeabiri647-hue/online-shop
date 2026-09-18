from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy() 
import time

def get_current_time():
    return round(time.time())