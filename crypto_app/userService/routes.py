from flask import Flask, Blueprint, request, render_template, url_for, flash, redirect, jsonify, make_response, current_app
from .forms import RegistrationForm, LoginForm
from .models import User
from .extensions import db, bcrypt
import uuid
import jwt
from datetime import datetime, timedelta
from functools import wraps


users = Blueprint('users', __name__, template_folder='templates/userService')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            print(data)
            current_user = User.query.filter_by(public_id=data['public_id']).first()
            if not current_user:
                raise Exception("User not found")
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401
        except Exception as e:
            return jsonify({'message': str(e)}), 401

        return f(current_user, *args, **kwargs)

    return decorated


@users.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(public_id=str(uuid.uuid4()), first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created!', 'success')
        return redirect(url_for('users.login'))
    return render_template('signup.html', form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        remember_me = form.remember.data

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            expiration_time = timedelta(days=7) if remember_me else timedelta(minutes=30)
            token_payload = {
                'public_id': user.public_id,
                'exp': datetime.utcnow() + expiration_time
            }
            token = jwt.encode(token_payload, current_app.config['SECRET_KEY'], algorithm='HS256')
            
            response = make_response(redirect(url_for('reading.home')))
            response.set_cookie('token', token, expires=datetime.utcnow() + expiration_time, secure=True, httponly=True, samesite='Strict')

            token_cookie = request.cookies.get('token')
            print("Token Cookie:", token_cookie)

            return response
        else:
            flash('Login unsuccessful. Please check your email and password.', 'danger')
            #return make_response(jsonify({'message': 'Invalid email or password', 401)

    #return jsonify({'message': 'Invalid input data'}), 400
    return render_template('login.html', form=form)




  

    if current_user.is_authenticated:
        return redirect(url_for('reading.records'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('reading.records'))
        else:
            flash(f'Login unsuccessful. Please check your email and password.', 'danger')
    return render_template('login.html', form=form)

@users.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    public_id = [user.public_id for user in users]
    return jsonify(public_id)

@users.route('/user/<public_id>', methods=['GET'])
def get_one_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message' : 'No user found!'})  
    return jsonify({'id': user.id, 'first_name': user.first_name, 'public_id': user.public_id})


@users.route('/user/<public_id>', methods=['DELETE'])
def delete_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message' : 'No user found!'})  
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message' : 'Your account has been deleted!'})  






    



@users.route('/logout')
def logout():
    response = make_response(redirect(url_for('frontend.index')))
    response.delete_cookie('token')

    return response