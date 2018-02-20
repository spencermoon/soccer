import data
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle
import warnings
warnings.filterwarnings("ignore")

def model(df):
	"""
	This function fits a logistic regression model on dataset provided by the user. It prints the model accuracy and creates a pickle file so that the model can be referenced later.
	
	Arg:
		df (DataFrame): data to be used for fitting the model
	"""

	# Specify fields that are numerical and categorical
	numerical = list(df.describe())
	categorical = ['buildUpPlaySpeedClass_home', 'buildUpPlayDribblingClass_home', 
    	           'buildUpPlayPassingClass_home', 'buildUpPlayPositioningClass_home', 'chanceCreationPassingClass_home',
        	       'chanceCreationCrossingClass_home', 'chanceCreationShootingClass_home', 'chanceCreationPositioningClass_home',
            	   'defencePressureClass_home', 'defenceAggressionClass_home', 'defenceTeamWidthClass_home',
            	   'defenceDefenderLineClass_home', 'team_long_name_home', 'buildUpPlaySpeedClass_away',
            	   'buildUpPlayDribblingClass_away', 'buildUpPlayPassingClass_away', 'buildUpPlayPositioningClass_away', 
            	   'chanceCreationPassingClass_away', 'chanceCreationCrossingClass_away', 'chanceCreationShootingClass_away', 
            	   'chanceCreationPositioningClass_away','defencePressureClass_away', 'defenceAggressionClass_away',
            	   'defenceTeamWidthClass_away', 'defenceDefenderLineClass_away', 'team_long_name_away']

	# Convert data type as 'category'
	for i in categorical:
		df[i] = df[i].astype('category')

	# Create dummy variables
	dummy = pd.get_dummies(df, columns = categorical)

	# Split data into response and predictors
	y = dummy['result']
	x = dummy.drop('result', axis = 1)

	# Create training and test data tables
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .3, random_state = 25)

	# Fit logistic regression model on training data
	logreg_train = LogisticRegression().fit(x_train, y_train)

	# Print out prediction accuracy for the data
	print('Model accuracy on training dataset: {:.2f}'.format(logreg_train.score(x_train, y_train)))
	print('Model accuracy on test dataset: {:.2f}'.format(logreg_train.score(x_test, y_test)))

	# Fit logistic regression model on entire dataset
	logreg = LogisticRegression().fit(x, y)

	# Create pickle file
	model_name = 'model.pkl'
	model_pkl = open(model_name, 'wb')
	pickle.dump(logreg, model_pkl)
	model_pkl.close()

if __name__ == "__main__":
    model(data.manipulate())


