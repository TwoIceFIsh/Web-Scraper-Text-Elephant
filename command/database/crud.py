import sqlite3
from sqlite3 import Error

DB_NAME = './datas.db'


def create_connection(db_name):
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except Error as e:
        print(e)
    return None


def do_sql(query_text: str):
    query_text = query_text.lower()
    db_connection = create_connection(DB_NAME)
    cursor_obj = db_connection.cursor()
    try:
        cursor_obj.execute(query_text)
        db_connection.commit()
    except Exception as e:
        return []
    finally:
        if 'select' in query_text:
            return cursor_obj.fetchall()
        cursor_obj.close()
        db_connection.commit()
        db_connection.close()
