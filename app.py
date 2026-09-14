from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from blueprint.general import app as general
from blueprint.admin import app as admin
from blueprint.user import app as user
import config
import extention
from flask_login import LoginManager
from models.user import User



app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(admin)
app.register_blueprint(general)

app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = config.SECRET_KEY
extention.db.init_app(app)
csrf = CSRFProtect(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


with app.app_context():
    extention.db.create_all()

if __name__ == '__main__':
    app.run(debug=True)