from flask import Flask
from .extensions import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(users_id):
    return User.query.get(int(users_id))

class User(db.Model, UserMixin):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String(60), nullable=False)
