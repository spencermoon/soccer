from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
import sqlalchemy

# Define application.
application = Flask(__name__)

# Configure SQLAlchemy.
application.config.from_object('config')
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

# Initialize the database.
db = SQLAlchemy(application)