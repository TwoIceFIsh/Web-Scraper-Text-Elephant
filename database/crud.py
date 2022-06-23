import sqlite3
from sqlite3 import Error

DB_NAME = './datas.db'


def create_db():
    con = sqlite3.connect(DB_NAME)


def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def db_select(query: str, concat: int):
    db_connection = create_connection(DB_NAME)
    cursor_obj = db_connection.cursor()
    cursor_obj.execute(query)
    row_list = cursor_obj.fetchall()

    if concat == 0:
        for row in row_list:
            print(row)
    else:
        print(row_list)
