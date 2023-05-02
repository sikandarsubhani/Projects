# __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

# Initialize LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///lesco.db'
app.config['SECRET_KEY']='1d42ece6b70dcbed3b4d7ce8'
db=SQLAlchemy(app)


from lesco import routes
