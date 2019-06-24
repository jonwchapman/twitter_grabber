from db_connection import db_connection
from get_user import get_user_id


def add_user(user_name, user_id):
    mydb = db_connection()
    stmt1 = "INSERT INTO user (user_id, user_name) VALUES (%s, %s)"
    try:
        cursor = mydb.cursor()
        cursor.execute(stmt1, (user_id, user_name))
        mydb.commit()
        return 0

    except Exception:
        # TODO: Add specific exceptions
        return 1
