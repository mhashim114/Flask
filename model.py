import sqlite3

def show_admin_pass(user):
    connection  = sqlite3.connect('learning-flask.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT password FROM users WHERE username = '{admin}'; """.format(admin = user))
    admin_pass = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    message = f'{user} password is {admin_pass}'

    return message

def create_account(username, password):
    connection = sqlite3.connect('learning-flask.db', check_same_thread = False)
    cursor = connection.cursor()

    cursor.execute(
    """INSERT INTO users(
        username,
        password
    )VALUES(
        '{username}',
        '{password}'
    );
    """.format(username = username, password = password)
)

    connection.commit()
    cursor.close()
    connection.close()

    message = "Account created successfully"
    return message

def user_exists(username, password):
    connection = sqlite3.connect('learning-flask.db', check_same_thread = False)
    cursor = connection.cursor()

    cursor.execute(""" select * from users where username = '{username}' and password = '{password}'; """.format(username = username, password = password))
    userFound = 0
    if cursor.fetchone() != None:
        userFound = 1
    
    connection.commit()
    cursor.close()
    connection.close()

    return userFound

def create_new_list(list_name):
    connection = sqlite3.connect('todo.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """ CREATE TABLE '{list_name}'(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            item VARCHAR(16),
            completed INTEGER(1)
        );""".format(list_name = list_name)
    )

    connection.commit()
    cursor.close()
    connection.close()

    message = "List created successfully"
    return message

def add_item_in_list(item, inList):
    connection = sqlite3.connect('todo.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """ INSERT INTO '{inList}'(
            item,
            completed
        )VALUES(
            '{item}',
            '{completed}'

        );""".format(inList = inList, item = item, completed = False)
    )

    connection.commit()
    cursor.close()
    connection.close()

    message = "New Item added successfully"
    return message

def show_all_lists():
    connection = sqlite3.connect('todo.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(""" SELECT name FROM sqlite_master WHERE type = 'table' AND name  NOT LIKE 'sqlite_%';""")
    tables = cursor.fetchall() 

    connection.commit()
    cursor.close()
    connection.close()

    return tables








