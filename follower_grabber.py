# designed to be run after fully populating database with users.
# This passes the id to the get_followers module, where it is used to look up the user_id from the db, and
# then grab the following data using twint.
from get_user import get_all_users
from get_followers import get_followers
from db_connection import db_connection


def set_processed(userid):
    stmt = "UPDATE `user` SET processed = 1 where id = %s"
    mydb = db_connection()

    try:
        cursor = mydb.cursor()
        cursor.execute(stmt, (userid))

    except:
        print("error in setting processed bit.")


print("Twitter Follower Grabber")
listOfUsers = get_all_users()
if listOfUsers == 1:
    print("")

else:
    index = 1

    for user_name in listOfUsers:
        if index < 3:
            user_id = get_followers(user_name[0])
            set_processed(user_id)

            index = index + 1
