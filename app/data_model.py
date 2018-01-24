from app import db

# Define data tables

class team(db.Model):

	__tablename__ = 'Team'

	team_id = db.Column('team_api_id', db.Integer, primary_key = True)
	team_name = db.Column('team_long_name', db.String(100))