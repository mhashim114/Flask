import sqlite3

connection = sqlite3.connect('learning-flask.db', check_same_thread=False)

cursor = connection.cursor()

cursor.execute(
    """ CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(16),
        password VARCHAR(16)
    );"""
)

connection.commit()
cursor.close()
connection.close()