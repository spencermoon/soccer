from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)
db_path = '../../data/data.sqlite'

#SQLALCHEMY_DATABASE_URI = 'sqlite:///../../data/database.sqlite'
#SQLALCHEMY_TRACK_MODIFICATIONS = True

# SQLAlchemy configuration
#app.config.from_envvar('SOCCER_SETTINGS', silent = True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

engine = create_engine('sqlite:///' + db_path)

# Initialize the database
db = SQLAlchemy(app)