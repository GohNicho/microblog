from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config') # Configure using config.py
db = SQLAlchemy(app) # THIS IS OUR DB OBJECT

from app import views, models # Database models.. not exactly MVC
