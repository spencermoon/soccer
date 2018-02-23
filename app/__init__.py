from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
import sqlalchemy

app = Flask(__name__)

# SQLAlchemy configuration
app.config.from_object('config')
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI)

#engine = create_engine('sqlite:///' + db_path)

# Initialize the database
db = SQLAlchemy(app)