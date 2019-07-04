# designed to be run after fully populating database with users.
# This passes the id to the get_followers module, where it is used to look up the user_id from the db, and
# then grab the following data using twint.
import sys
from get_user import get_all_users
from get_followers import get_followers


print("Twitter Follower Grabber")
print(sys.argv[1])
print(sys.argv[2])

listOfUsers = get_all_users(sys.argv[1], sys.argv[2])
if listOfUsers == 1:
    print("")

else:
    for user_name in listOfUsers:
        get_followers(user_name[0])

