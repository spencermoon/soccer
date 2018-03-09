
# Local database
#SQLALCHEMY_DATABASE_URI = 'sqlite:///../../data/data.sqlite'
#LOCAL_PATH = '../data/data.sqlite'
DB_PATH = '../../data/database.sqlite'

# RDS database
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://spencer:msia_423@db.c70edrasw7bt.us-west-2.rds.amazonaws.com:3306/epl'


SQLALCHEMY_TRACK_MODIFICATIONS = False
#SECRET_KEY = 'sbQm38a1awYXbmfWLgZaHCupa8egevTiZusvHx/G'
