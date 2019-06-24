import twint

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
