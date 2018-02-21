from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)

# SQLAlchemy configuration
app.config.from_object('config')

#engine = create_engine('sqlite:///' + db_path)

# Initialize the database
db = SQLAlchemy(app)