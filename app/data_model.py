from app import db


class team(db.Model):
	"""Define columns for teams."""
	__tablename__ = 'teams'

	team_id = db.Column('team_api_id', db.Integer, primary_key = True)
	team_name = db.Column('team_long_name', db.String(100))


class stat(db.Model):
	"""Define columns for stats."""
	__tablename__ = 'stats'

	season_year = db.Column('season_year', db.Integer, primary_key = True)
	buildUpPlaySpeed_home = db.Column('buildUpPlaySpeed_home', db.Integer)
	buildUpPlaySpeedClass_home = db.Column('buildUpPlaySpeedClass_home', db.String(100))
	buildUpPlayDribblingClass_home = db.Column('buildUpPlayDribblingClass_home', db.String(100))
	buildUpPlayPassing_home = db.Column('buildUpPlayPassing_home', db.Integer)
	buildUpPlayPassingClass_home = db.Column('buildUpPlayPassingClass_home', db.String(100))
	buildUpPlayPositioningClass_home = db.Column('buildUpPlayPositioningClass_home', db.String(100))
	chanceCreationPassing_home = db.Column('chanceCreationPassing_home', db.Integer)
	chanceCreationPassingClass_home = db.Column('chanceCreationPassingClass_home', db.String(100))
	chanceCreationCrossing_home = db.Column('chanceCreationCrossing_home', db.Integer)
	chanceCreationCrossingClass_home = db.Column('chanceCreationCrossingClass_home', db.String(100))
	chanceCreationShooting_home = db.Column('chanceCreationShooting_home', db.Integer)
	chanceCreationShootingClass_home = db.Column('chanceCreationShootingClass_home', db.String(100))
	chanceCreationPositioningClass_home = db.Column('chanceCreationPositioningClass_home', db.String(100))
	defencePressure_home = db.Column('defencePressure_home', db.Integer)
	defencePressureClass_home = db.Column('defencePressureClass_home', db.String(100))
	defenceAggression_home = db.Column('defenceAggression_home', db.Integer)
	defenceAggressionClass_home = db.Column('defenceAggressionClass_home', db.String(100))
	defenceTeamWidth_home = db.Column('defenceTeamWidth_home', db.Integer)
	defenceTeamWidthClass_home = db.Column('defenceTeamWidthClass_home', db.String(100))
	defenceDefenderLineClass_home = db.Column('defenceDefenderLineClass_home', db.String(100))
	team_long_name_home = db.Column('team_long_name_home', db.String(100))
	buildUpPlaySpeed_away = db.Column('buildUpPlaySpeed_away', db.Integer)
	buildUpPlaySpeedClass_away = db.Column('buildUpPlaySpeedClass_away', db.String(100))
	buildUpPlayDribblingClass_away = db.Column('buildUpPlayDribblingClass_away', db.String(100))
	buildUpPlayPassing_away = db.Column('buildUpPlayPassing_away', db.Integer)
	buildUpPlayPassingClass_away = db.Column('buildUpPlayPassingClass_away', db.String(100))
	buildUpPlayPositioningClass_away = db.Column('buildUpPlayPositioningClass_away', db.String(100))
	chanceCreationPassing_away = db.Column('chanceCreationPassing_away', db.Integer)
	chanceCreationPassingClass_away = db.Column('chanceCreationPassingClass_away', db.String(100))
	chanceCreationCrossing_away = db.Column('chanceCreationCrossing_away', db.Integer)
	chanceCreationCrossingClass_away = db.Column('chanceCreationCrossingClass_away', db.String(100))
	chanceCreationShooting_away = db.Column('chanceCreationShooting_away', db.Integer)
	chanceCreationShootingClass_away = db.Column('chanceCreationShootingClass_away', db.String(100))
	chanceCreationPositioningClass_away = db.Column('chanceCreationPositioningClass_away', db.String(100))
	defencePressure_away = db.Column('defencePressure_away', db.Integer)
	defencePressureClass_away = db.Column('defencePressureClass_away', db.String(100))
	defenceAggression_away = db.Column('defenceAggression_away', db.Integer)
	defenceAggressionClass_away = db.Column('defenceAggressionClass_away', db.String(100))
	defenceTeamWidth_away = db.Column('defenceTeamWidth_away', db.Integer)
	defenceTeamWidthClass_away = db.Column('defenceTeamWidthClass_away', db.String(100))
	defenceDefenderLineClass_away = db.Column('defenceDefenderLineClass_away', db.String(100))
	team_long_name_away = db.Column('team_long_name_away', db.String(100))