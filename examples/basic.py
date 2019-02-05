import psycopg2
from datetime import datetime

def make_users(count=100):
    connect = psycopg2.connect(database='predicto', host='localhost', port=5432, user='predicto', password='predicto')
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS predicto(id SERIAL PRIMARY KEY, name TEXT NOT NULL, created TIMESTAMP);")
    cursor.execute('INSERT INTO predicto(name, created) VALUES (%s, %s)', ('user', datetime.now()))
    connect.close()

make_users()