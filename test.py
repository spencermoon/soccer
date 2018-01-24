from flask import render_template
from app import db, app
from app.data_model import team 

@app.route('/')
def index():
	
	return render_template('index.html', teams = team.query.all())

if __name__ == "__main__":
	app.run(debug = True)
