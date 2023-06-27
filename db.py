import psycopg2
from flask import g

DATABASE = {
    "host": "localhost",
    "port": "5432",
    "database": "nbp",
    "user": "postgres",
    "password": "adriblack24"
}

def get_conn():
    if 'db' not in g:
        g.db = psycopg2.connect(
            host=DATABASE["host"],
            port=DATABASE["port"],
            database=DATABASE["database"],
            user=DATABASE["user"],
            password=DATABASE["password"]
        )

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()