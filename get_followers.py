def get_followers(id):
    d = twint.Config()

    d.User_id = id
    d.Store_object = True
    d.Hide_output = True
    d.Format = "{user_id}"

    try:
        print("Trying to get followers....")
        twint.run.Followers(d)
        followers_dict = twint.output.follow_object
        index = 1
        for x in followers_dict:
            print(index)
            print("followee: " + x)
            index = index + 1

            followers = followers_dict[x].get("followers")

            for name in followers:
                print("follower:" + name)
                uid = get_userid(name)
                print("UID: " + uid)
                #store_follower(uid)

        print(" ")
        print(" ")

    except:
        print("ERROR - UNABLE TO RETRIEVE FOLLOWERS")


def get_count():
    stmt = "SELECT COUNT(*) FROM user limit 10"
    cursor.execute(stmt)
    count_val = cursor.fetchone()
    return count_val




count = get_count()
counter = count[0]

# REMOVE
counter = 20

while counter > 0:
    print(counter)
    count_tup = (counter,)
    ret_val = get_user(count_tup)
    if type(ret_val) == tuple:
        # print(ret_val[0])
        print(ret_val[1])
        get_followers(ret_val[1])

    counter = counter - 1

