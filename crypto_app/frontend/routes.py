from flask import Blueprint, render_template, url_for, request, current_app, redirect
import jwt
from datetime import datetime

frontend = Blueprint('frontend', __name__, template_folder='templates/frontend')


@frontend.route("/")
def index():
    token_cookie = request.cookies.get('token')
    print(token_cookie)
    
    if token_cookie:
        try:
            decoded_token = jwt.decode(token_cookie, current_app.config['SECRET_KEY'], algorithms=['HS256'])   
            token_exp = datetime.fromtimestamp(decoded_token['exp'])
            
            if token_exp > datetime.utcnow():
                return redirect(url_for('reading.home'))
            
        except jwt.ExpiredSignatureError:
            return render_template('index.html')
        except jwt.InvalidTokenError:
            return render_template('index.html')
    
    return render_template('index.html')