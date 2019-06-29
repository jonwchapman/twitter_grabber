import twint

from add_user import add_user
from add_follower import add_follower
from get_user import get_user_id
from set_processed import set_processed


def get_followers(name):
    d = twint.Config()

    d.Username = name
    d.Store_object = True
    d.Hide_output = True
    d.Format = "{user_id},{user_name}"

    try:
        twint.run.Followers(d)
        followers_dict = twint.output.follow_object

        followers = followers_dict[name]["followers"]
        follower_id = get_user_id(name)

        print("######### Adding Followers for " + name + " ###########")

        for followee in followers:
            print("Adding follower " + followee + " for user " + name)
            followee_id = get_user_id(followee)
            add_user(followee, followee_id)
            add_follower(follower_id, followee_id)

        print("######### Done with user " + name + " ###############")

        set_processed(name, 1)
        return 0

    except:
        print("Error in retrieving followers.")
        set_processed(name, 2)
        return 1
