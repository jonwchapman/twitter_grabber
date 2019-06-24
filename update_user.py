from db_connection import db_connection
import mysql.connector


def update_user(user_name, user_id):
    print("updating user_id now.")
    mydb = db_connection()

    try:
        stmt1 = "UPDATE `user` SET user_id = %s where user_name = %s"
        cursor = mydb.cursor()
        cursor.execute(stmt1, (user_id, user_name))
        mydb.commit()

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    return 0
