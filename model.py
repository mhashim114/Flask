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

def login(username , password):
    connection = sqlite3.connect('learning-flask.db', check_same_thread = False)
    cursor = connection.cursor()

    cursor.execute(""" select * from users where username = '{username}'; """.format(username = username))
    userFound = 0
    if cursor.fetchone() != None:
        userFound = 1
    
    connection.commit()
    cursor.close()
    connection.close()

    return userFound










