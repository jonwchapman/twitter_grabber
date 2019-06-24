from db_connection import db_connection
import twint


def get_user(search=None):
    mydb = db_connection()
    cursor = mydb.cursor()
    if type(search) == 'int':
        stmt = "SELECT * FROM user where id = %s"
    elif search is None:
        stmt = "SELECT user_name FROM user"
    else:
        stmt = "SELECT * FROM user WHERE user_name = %s"

    try:
        if search is not None:
            cursor.execute(stmt, search)
        else:
            result = cursor.execute(stmt)
            return result

        result = cursor.fetchone()
        return result

    except Exception as e:
        print("Error '{0}' occured. Arguments {1}.".format(e.message, e.args))
        return 1


def get_all_users():
    mydb = db_connection()
    cursor = mydb.cursor()
    stmt = "SELECT user_name from user order by influenze_project desc"
    cursor.execute(stmt)
    result = cursor.fetchall()

    return result


def get_user_id(name):
    print("get_user_id called for user: " + name)
    d = twint.Config()
    d.Username = name
    d.Store_object = True
    d.Hide_output = True

    try:
        twint.run.Lookup(d)
        users = twint.output.user_object
        for user in users:
            print(user.username)
            print(user.id)
        twint.output.user_object = []

    except:
        exception = 1

    return user.id


