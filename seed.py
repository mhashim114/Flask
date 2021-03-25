import sqlite3

connection = sqlite3.connect('learning-flask.db', check_same_thread=False)

cursor = connection.cursor()

cursor.execute(
    """INSERT INTO users(
        username,
        password
    )VALUES(
        'admin',
        'admin'
    );
    """
)

connection.commit()
cursor.close()
connection.close()