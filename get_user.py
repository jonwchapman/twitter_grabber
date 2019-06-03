def get_user(search):
    if type(search) == 'int':
        stmt = "SELECT * FROM user where id = %s"
    else:
        stmt = "SELECT * FROM user WHERE user_name = %s"

    try:
        cursor.execute(stmt, search)
        result = cursor.fetchone()
        return result

    except:
        print("ERROR IN GETTING USER")
        return 1


def get_userid(name):
    print("get_userid called for user: " + name)
    try:
        stmt = "SELECT user_id FROM user WHERE user_name = %s "
        name_tup = (name,)
        print(name_tup)
        cursor.execute(stmt, name_tup)
        result = cursor.fetchone()
        uid = result[0]
    except:
        if flag is None:
            flag = 1
            retrieve_user()
            get_userid(name)
        else:
            uid = 0

    return id
