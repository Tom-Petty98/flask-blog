from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= str(getenv('FLASK_BLOG_DB_URI'))
db = SQLAlchemy(app)

from application import routes

