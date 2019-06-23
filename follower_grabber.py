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
        print("Trying to get followers for user " + name + ".")
        twint.run.Followers(d)
        followers_dict = twint.output.follow_object
        # index = 1
        try:
            followers = followers_dict[name]["followers"]
            for x in followers:
                #should probably perform a check before adding this willy-nilly
                add_user(x)

                print("Adding follower " + x + " for user " + name)
                follower_id = get_user_id(name)
                followee_id = get_user_id(x)
                add_follower(follower_id, followee_id)

            print("done with user " + name + ".")

        except:
            print("")

        # for x in followers_dict:
        #     print(index)
        #     print("followee: " + x)
        #     index = index + 1
        #     followers = followers_dict[x].get("followers")
        #
        #     for name in followers:
        #         print("follower:" + name)
        #         uid = get_userid(name)
        #         print("UID: " + uid)
        #         store_follower(uid)

    except:
        print("ERROR - UNABLE TO RETRIEVE FOLLOWERS")

    return


listOfUsers = get_all_users()
if listOfUsers == 1:
    print("")
else:
    for user_name in listOfUsers:
        get_followers(user_name[0])
