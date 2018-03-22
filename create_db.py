from app import db
import app.data_model

def create_db():
	"""Create database."""
    db.create_all()

if __name__ == '__main__':
    create_db()
    print('Database created.')