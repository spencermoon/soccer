from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
import sqlalchemy

application = Flask(__name__)

# SQLAlchemy configuration
application.config.from_object('config')
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

# Initialize the database
db = SQLAlchemy(application)