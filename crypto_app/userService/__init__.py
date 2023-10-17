from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
#from .config import UserConfig
from .models import User
from .extensions import db

#users_blueprint = Blueprint('users', __name__)


# def create_app(app):
#     app = Flask(__name__)

#     app.config.from_object(UserConfig)
#     db.init_app(app)

#     with app.app_context():
#         db.create_all()
  
#     return app
