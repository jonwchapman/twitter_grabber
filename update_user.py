from db_connection import db_connection
from set_processed import set_id_processed
import mysql.connector


def update_user(user_name, user_id):
    mydb = db_connection()

    if user_id != 0:
        try:
            stmt1 = "UPDATE `user` SET user_id = %s where user_name = %s"
            cursor = mydb.cursor()
            cursor.execute(stmt1, (user_id, user_name))
            mydb.commit()
            set_id_processed(user_name, 1)
            return 0

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return 1

    else:
        set_id_processed(user_name, 2)
