# Predicting English Premier League Match Results

This is the libarary for my [application](http://match-prediction.us-west-2.elasticbeanstalk.com/) that predicts EPL match results. 


## Motivation

I wanted to create an application that helps answer one of the most fundamental questions for sports fans: who will win? As an avid football fan, I wanted to build an app for fans to interact with and obtain match predictions for the English Premier League. This app allows users to select teams for the home and away sides and produces win probabilities based on the user inputs.


## Directory Organization

You can navigate this library using the following mapping:


    ├── app                    # Source code for setting up Flask & SQLAlchemy
    ├── develop                 
    │   ├── data.py            # Scripts for data ingestion
    │   ├── model.py           # Scripts for creating the predictive model 
    │   ├── prediction.py      # Scripts for making predictions
    │   ├── test.py            # Unit tests for the above functions
    │   └── eda.ipynb          # Notebook for exploratory data analysis
    ├── docs                   # Sphinx documentation
    ├── static                 # Background images for the web application
    ├── application.py         
    ├── config.py              # AWS Elastic Beanstalk and Flask configuration   
    ├── create_db.py                
    └── requirements.txt       # Requirements for running the application


## Data & Model

I used the [European Soccer Database](https://www.kaggle.com/hugomathien/soccer/data) from Kaggle for this application. The dataset consists of historical match results for a number of European leagues, teams and their attributes (e.g. offensive style and overall team rating), and other player information. I filtered the data to include just the EPL matches across 32 teams before fitting the model. 

I fit a multinomial logistic regression model on the ingested data to predict which side would win the match. The predictors mainly consist of team attributes for both the home and away sides. To reproduce the model, please follow these steps:

1. Clone this repository.

2. Create a conda environment for the app.

    `conda create -n app python=3`
    
3. Activate environment and set your path to the repo.

    `source activate app`

4. Install required packages.

    `pip install -r requirements.txt`
    
5. Download the Kaggle database and place it in a folder outside the repo.

6. In `config.py`, change the local pathway for the database that you have just downloaded.

    `DB_PATH = '../../data/database.sqlite'`

7. Change your path to the `develop` folder within the root directory and run the following commands.

    `cd ./develop/`
    
    `python model.py`

8. Running the command above saves the model as a pickle file, which can be loaded to make predictions. Logs from data ingestion and model creation can be found in `log.log`.


## Unit Testing

Unit tests can be conducted by running the following commands:

    cd ./develop/
    pytest test.py


## Documentation

The documentation for the functions found in this library can be accessed by opening this [file](https://github.com/spencermoon/soccer/blob/master/docs/_build/html/index.html) in your browser after cloning the repository. 


## Pivotal Tracker

The development process for this application can be found here: [Pivotal Tracker](https://www.pivotaltracker.com/n/projects/2141794).
