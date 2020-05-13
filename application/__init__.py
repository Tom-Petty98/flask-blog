from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from os import getenv

app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

app.config['SQLALCHEMY_DATABASE_URI']= str(getenv('FLASK_BLOG_DB_URI'))
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
db = SQLAlchemy(app)
login_manager.login_view = 'login'

from application import routes

