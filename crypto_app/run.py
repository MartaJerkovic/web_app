import os
from flask import Flask
from frontend.routes import frontend
from userService.routes import users
from readingService.routes import reading
from csvService.routes import data_processing
from userService.extensions import db as db_users
#from csvService.extensions import db as db_transactions


app = Flask(__name__)

db_users_folder = os.path.join(app.root_path, 'userService')
db_transactions_folder = os.path.join(app.root_path, 'csvService')

app.config['SECRET_KEY'] = 'DOINEEDTHISSECRETKEY?'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(db_users_folder, 'users.db')
app.config['SQLALCHEMY_BINDS'] = {'transactions' : 'sqlite:///' + os.path.join(db_transactions_folder, 'transactions.db')}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db_users.init_app(app)
#db_transactions.init_app(app)

    # with app.app_context():
    #     db_users.create_all()
    #     db_transactions.create_all()


app.register_blueprint(frontend)
app.register_blueprint(users)
app.register_blueprint(reading)
app.register_blueprint(data_processing)


if __name__ == '__main__':
    app.run(debug=True)


 