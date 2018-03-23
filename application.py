from flask import render_template, request, redirect, url_for, flash
from app import application, db, engine
from app.data_model import team
from develop.prediction import prediction
from sklearn.externals import joblib
import pandas as pd


@application.route('/')
def index():
	"""Render template for home page."""
	return render_template('index.html', teams = team.query.all())


@application.route('/result', methods = ['POST'])
def result():
	"""Render template for result page."""

	# Make a prediction based on user inputs from home page. 
	if request.method == 'POST' and request.form['mainbutton'] == 'submitted':
		home = request.form.get('hometeam')
		away = request.form.get('awayteam')
		stats = pd.read_sql_query("select * from stats;", engine)
		model = joblib.load('./develop/model.pkl')
		result = prediction(home, away, stats, model)

		return render_template('result.html', result = result, home = home, away = away)
	
	# Return to home page if no user selections are made.
	else:
		return redirect(url_for('index'))

if __name__ == "__main__":
	application.run(host = '0.0.0.0', debug = True)