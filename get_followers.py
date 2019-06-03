import twint
import mysql.connector
from os import system, name

val = (1,)
count_tup = ((),)
followee_id = 0
mydb = mysql.connector.connect(
  host="localhost",
  user="twitter_admin",
  passwd="EyPxGqpK1y0v53rU",
  database="twitter"
)
cursor = mydb.cursor()

c = twint.Config()
c.Limit = 100
c.Hide_output = True
c.User_id = 0
c.Store_object = True


def logger():
    return


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

