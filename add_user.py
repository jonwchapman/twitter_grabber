def add_user(user_id, user_name, mydb):
    stmt1 = "INSERT INTO user (user_id, user_name) VALUES (%s, %s)"

    try:
        cursor = mydb.cursor()
        cursor.execute(stmt1, (user_id, user_name))
        mydb.commit()
        return 1

    except Exception:
        #logger()
        return 0
