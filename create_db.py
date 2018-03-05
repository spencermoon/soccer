from app import db

def create_db():
    db.create_all()

if __name__ == '__main__':
    create_db()
    print('Database created.')