# primary use is to know how many times to loop if we are conducting some action against users within the database.
def get_user_count():
    # limit 10 is present purely for debugging purposes
    stmt = "SELECT COUNT(*) FROM user limit 10"
    cursor.execute(stmt)
    count_val = cursor.fetchone()
    return count_val

