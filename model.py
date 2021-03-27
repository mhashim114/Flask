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
