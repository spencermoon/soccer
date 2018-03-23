import data, prediction
import pandas as pd
import numpy as np
import sys
from sklearn.externals import joblib
sys.path.append("..")
from app import engine


def test_data():
	"""Test data.py for column count and data type."""
	
	# Create DataFrame.
	df = data.manipulate()

	# Check type of output.
	assert isinstance(df, pd.DataFrame)

	# Check column count.
	assert len(df.columns) == 44


def test_predict():
	"""Test predict.py for array length and data type."""
	
	# Create a row of data and run prediction.
	home = 'Arsenal'
	away = 'Chelsea'
	stats = pd.read_sql_query("select * from stats;", engine)
	model = joblib.load('./model.pkl')
	result = prediction.prediction(home, away, stats, model)

	# Check type of output.
	assert isinstance(result, np.ndarray)

	# Check array length.
	assert len(result) == 3

