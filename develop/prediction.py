import datetime
from sklearn.externals import joblib
import pickle
import pandas as pd


def prediction(home, away, stats, model):
    """Make predictions using a static model.

    This function returns win probabilities based on user inputs for home and 
    away teams combined with team attributes and playing styles.

    Args:
        home (str): Home team name.
        away (str): Away team name.
        stats (df): DataFrame that contains team attributes and playing styles.
        model (pkl): Static model.

    Returns:
        list: List of win probabilities for away, draw, and home.
    """

    # Define categorical variables and initiate year variable.
    categorical = ['buildUpPlaySpeedClass_home', 'buildUpPlayDribblingClass_home',
                   'buildUpPlayPassingClass_home', 'buildUpPlayPositioningClass_home', 
                   'chanceCreationPassingClass_home', 'chanceCreationCrossingClass_home', 
                   'chanceCreationShootingClass_home', 'chanceCreationPositioningClass_home',
                   'defencePressureClass_home', 'defenceAggressionClass_home', 
                   'defenceTeamWidthClass_home', 'defenceDefenderLineClass_home', 
                   'team_long_name_home', 'buildUpPlaySpeedClass_away',
                   'buildUpPlayDribblingClass_away', 'buildUpPlayPassingClass_away', 
                   'buildUpPlayPositioningClass_away', 'chanceCreationPassingClass_away', 
                   'chanceCreationCrossingClass_away', 'chanceCreationShootingClass_away',
                   'chanceCreationPositioningClass_away', 'defencePressureClass_away', 
                   'defenceAggressionClass_away', 'defenceTeamWidthClass_away', 
                   'defenceDefenderLineClass_away', 'team_long_name_away']
    year = datetime.datetime.now().year

    # Create dummy variables.
    stats = pd.get_dummies(stats, columns=categorical)

    # Map team attributes and playing styles for home and away teams.
    test = stats[(stats['team_long_name_home_' + home.replace(' ', '')] == 1)
                 & (stats['team_long_name_away_' + away.replace(' ', '')] == 1)]
    test['season_year'] = year

    # Make prediction from the loaded logistic regression model.
    predict = model.predict_proba(test)[0]

    return predict