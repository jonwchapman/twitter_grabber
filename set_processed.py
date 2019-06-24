from db_connection import db_connection
import mysql.connector


def set_processed(userid):
    stmt = "UPDATE `user` SET processed = 1 where user_id = %s"
    mydb = db_connection()

    try:
        cursor = mydb.cursor()
        cursor.execute(stmt, (userid,))
        mydb.commit()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))


def set_id_processed(username, code=1):
    stmt = "UPDATE `user` SET id_processed = %s where user_name = %s"
    mydb = db_connection()

    try:
        cursor = mydb.cursor()
        cursor.execute(stmt, (code, username))
        mydb.commit()

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
