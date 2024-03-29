from db_connection import db_connection
import mysql.connector


def add_user(user_name, user_id):
    print("adding user now.")
    mydb = db_connection()
    stmt1 = "INSERT INTO user (user_id, user_name) VALUES (%s, %s)"
    try:
        cursor = mydb.cursor()
        cursor.execute(stmt1, (user_id, user_name))
        mydb.commit()
        return 0

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
