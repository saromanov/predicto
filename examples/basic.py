import psycopg2
from datetime import datetime, timedelta
import random 
import string

def make_users(count=100):
    connect = psycopg2.connect(database='predicto', host='localhost', port=5432, user='predicto', password='predicto')
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS predicto(id SERIAL PRIMARY KEY, name TEXT NOT NULL, created TIMESTAMP);")
    for i in range(count):
        user = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        cursor.execute('INSERT INTO predicto(name, created) VALUES (%s, %s)', (user, datetime.now() - timedelta(hours=random.randint(1,30))))
    connect.close()

make_users()