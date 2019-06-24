# designed to be run after fully populating database with users.
# This passes the id to the get_followers module, where it is used to look up the user_id from the db, and
# then grab the following data using twint.
import json
import twint

from get_user import get_all_users
from add_user import add_user
from add_follower import add_follower
from get_user import get_user_id


def get_followers(name):
    d = twint.Config()

    d.Username = name
    d.Store_object = True
    d.Hide_output = True
    d.Format = "{user_id},{user_name}"

    try:
        twint.run.Followers(d)
        followers_dict = twint.output.follow_object

        try:
            followers = followers_dict[name]["followers"]
            follower_id = get_user_id(name)

            print("######### Adding Followers for " + name + " ###########")

            for followee in followers:
                print("Adding follower " + followee + " for user " + name)
                followee_id = get_user_id(followee)
                add_user(followee, followee_id)
                add_follower(follower_id, followee_id)

            print("######### Done with user " + name + " ###############")

        except:
            print("")

        # for x in followers_dict:
        #     print(index)
        #     print("followee: " + x)
        #     index = index + 1
        #     followers = followers_dict[x].get("followers")

        #     for name in followers:
        #         print("follower:" + name)
        #         uid = get_userid(name)
        #         print("UID: " + uid)
        #         store_follower(uid)

    except:
        print("ERROR - UNABLE TO RETRIEVE FOLLOWERS")

    return


print("Twitter Follower Grabber")
listOfUsers = get_all_users()
if listOfUsers == 1:
    print("")

else:
    index = 1

    for user_name in listOfUsers:
        if index < 3:
            get_followers(user_name[0])
            index = index + 1
