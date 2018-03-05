from app import db

def create_db():
    db.create_all()

if __name__ == '__main__':
    create_db()
    #print(db.engine.table_names())
    print('Database created.')