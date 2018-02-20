import datetime
from sklearn.externals import joblib
import pickle
import pandas as pd


def prediction(home, away, stats):
    categorical = ['buildUpPlaySpeedClass_home', 'buildUpPlayDribblingClass_home', 
    	           'buildUpPlayPassingClass_home', 'buildUpPlayPositioningClass_home', 'chanceCreationPassingClass_home',
        	       'chanceCreationCrossingClass_home', 'chanceCreationShootingClass_home', 'chanceCreationPositioningClass_home',
            	   'defencePressureClass_home', 'defenceAggressionClass_home', 'defenceTeamWidthClass_home',
            	   'defenceDefenderLineClass_home', 'team_long_name_home', 'buildUpPlaySpeedClass_away',
            	   'buildUpPlayDribblingClass_away', 'buildUpPlayPassingClass_away', 'buildUpPlayPositioningClass_away', 
            	   'chanceCreationPassingClass_away', 'chanceCreationCrossingClass_away', 'chanceCreationShootingClass_away', 
            	   'chanceCreationPositioningClass_away','defencePressureClass_away', 'defenceAggressionClass_away',
            	   'defenceTeamWidthClass_away', 'defenceDefenderLineClass_away', 'team_long_name_away']


    year = datetime.datetime.now().year
    model = joblib.load('./develop/model.pkl')
    stats = pd.get_dummies(stats, columns = categorical)

    test = stats[(stats['team_long_name_home_' + home.replace(' ','')] == 1) & (stats['team_long_name_away_' + away.replace(' ','')] == 1)]
    test['season_year'] = year

    predict = model.predict_proba(test)[0]

    return  predict
