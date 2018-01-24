from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db_path = '../../data/database.sqlite'

# SQLAlchemy configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Initialize the database
db = SQLAlchemy(app)
