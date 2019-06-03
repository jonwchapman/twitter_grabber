def get_user_count():
    # limit 10 is present purely for debugging purposes
    stmt = "SELECT COUNT(*) FROM user limit 10"
    cursor.execute(stmt)
    count_val = cursor.fetchone()
    return count_val

