from flask import render_template, request, redirect, url_for, flash
from app import app, db#, db_path, engine
from app.data_model import team, stat
from develop.prediction import prediction
import pandas as pd
import sqlite3

@app.route('/')
def index():

	return render_template('index.html', teams = team.query.all())


@app.route('/result', methods = ['POST'])
def result():

	if request.method == 'POST' and request.form['mainbutton'] == 'submitted':
		home = request.form.get('hometeam')
		away = request.form.get('awayteam')
		#stats = pd.read_sql(stat.query.all(), db)
		#stats.to_csv('test.csv')
		columns = stat.__table__.columns.keys()

		conn = sqlite3.connect("../data/data.sqlite")
		stats = pd.read_sql_query("select * from stats;", conn)
		


		result = prediction(home, away, stats)

		return render_template('result.html', result = result, home = home, away = away)
	
	else:
		return redirect(url_for('index'))

if __name__ == "__main__":
	app.run(debug = True)