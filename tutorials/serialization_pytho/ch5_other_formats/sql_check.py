
import sqlite3
from random import choice
from datetime import datetime, timedelta






with sqlite3.connect('logs.py') as db:

    with open('sql_example.sql', 'r') as fp:
        schema_sql = fp.read()
    db.executescript(schema_sql)
    db.commit()


    # generate some random data
    cur = db.cursor()
    now = datetime.now()
    insert_sql = 'INSERT INTO logs (time, level, message) values (?, ?, ?)'
    for i in range(10_000):
        time = now - timedelta(seconds=i)
        level = choice(['INFO', 'WARNING', 'ERROR'])
        message = f'log message #{i}'
        cur.execute(insert_sql, (time, level, message))
    db.commit()


# Query the database
with sqlite3.connect('logs.py') as db:
    db.row_factory = sqlite3.Row
    cur = db.cursor()
    query_select = 'SELECT * FROM logs WHERE level = "INFO" LIMIT 5'
    for row in cur.execute(query_select):
        print(dict(row))
