import pandas as pd
import sqlite3
import numpy as np

def read(name, db):
	"""
	This function creates a DataFrame for tables that exist in a sqlite database.

	Args:
		name (str): Name of the data table
		db (str): Database path

	Returns:
		DataFrame: Entire specified data table
	"""
    
    # Make connection with the database
	conn = sqlite3.connect(db)
	df = pd.read_sql_query("select * from " + name + ';', conn)
    
    # Print loaded data table name and return DataFrame
	print(name + ': loaded')
	return df


def manipulate(league_id = 1729):
	"""
	This function creates a DataFrame for data to be used for model fitting. It conducts a number of joins and variable selections to get to the final set of predictors.
	
	Arg:
		league_id (int): Defaults to EPL league ID

	Returns:
		DataFrame: Final dataset to be used for model fitting 
	"""

	# Define path for database
	db = '../../data/database.sqlite'

	# Load data tables
	match = read('match', db)
	team = read('team', db)
	team_attributes = read('team_attributes', db)

	# Create a column to specify which team won the match; this will server as the response variable in the model
	epl_matches = match[(match['league_id'] == league_id)]
	epl_matches['result'] = np.where(epl_matches['home_team_goal'] > epl_matches['away_team_goal'], 'home' , 
                        	np.where(epl_matches['home_team_goal'] == epl_matches['away_team_goal'], 'draw' , 'away'))

	# Create a field for season year
	epl_matches['season_year'] = pd.to_numeric(epl_matches['season'].str[:4])

	# Leave out unnecessary attributes
	epl_matches = epl_matches[['match_api_id', 'league_id', 'season_year', 'home_team_api_id', 'away_team_api_id', 'result']].reset_index(drop = True)

	# Create an mapping of EPL teams 
	epl_mapping = pd.DataFrame(pd.concat([epl_matches['home_team_api_id'], epl_matches['away_team_api_id']], ignore_index = True).unique())
	epl_mapping.columns = ['team_api_id']

	# Filter out data to only include EPL teams
	epl_teams = team_attributes.merge(epl_mapping, on = 'team_api_id', how = 'inner')

	# Create a column for year
	epl_teams['year'] = pd.DatetimeIndex(epl_teams['date']).year

	# Add team name and drop other  unnecessary fields
	epl_teams = epl_teams.merge(team[['team_api_id', 'team_long_name']], on = 'team_api_id', how = 'left').drop(['id', 'team_fifa_api_id', 'date'], axis = 1)

	# Add home team attributes
	data = pd.merge(epl_matches, epl_teams, how = 'inner', left_on = ['home_team_api_id', 'season_year'], right_on = ['team_api_id', 'year'])
	data = pd.merge(data, epl_teams, how = 'inner', left_on = ['away_team_api_id', 'season_year'], right_on = ['team_api_id', 'year'], suffixes = ('_home', '_away')) \
         	 .drop(['league_id', 'year_home', 'year_away', 'match_api_id', 'buildUpPlayDribbling_home', 'buildUpPlayDribbling_away', 'home_team_api_id', 'away_team_api_id', 'team_api_id_home', 'team_api_id_away'], axis = 1)

    # Return DataFrame
	return data
