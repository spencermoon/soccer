import pandas as pd
import sqlite3

def read(name, db):
    
    conn = sqlite3.connect(db)
    df = pd.read_sql_query("select * from " + name + ';', conn)
    
    print(name + ': loaded')
    return df