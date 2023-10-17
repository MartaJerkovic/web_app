import os
from flask import Flask
from frontend.routes import frontend
from userService.routes import users
from readingService.routes import reading
from userService.extensions import db, login_manager

app = Flask(__name__)

db_folder = os.path.join(app.root_path, 'userService')


app.config['SECRET_KEY'] = 'DOINEEDTHISSECRETKEY?'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(db_folder, 'users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager.init_app(app)

# with app.app_context():
#     db.create_all()

app.register_blueprint(frontend)
app.register_blueprint(users)
app.register_blueprint(reading)




if __name__ == '__main__':
    app.run(debug=True)
