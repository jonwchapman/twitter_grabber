import twint
from get_user_count import get_user_count
from add_user import add_user
from db_connection import db_connection


count = get_user_count()
counter = count[0]

# REMOVE
counter = 20

while counter > 0:
    print(counter)
    count_tup = (counter,)
    ret_val = get_user(count_tup)
    # check the return value to ensure its a tuple. If not a tuple, then its an error.
    if type(ret_val) == tuple:
        # print(ret_val[0])
        # print the user_id in the form of ret_val[1], can be removed after everything is working.
        print(ret_val[1])
        # pass the user_id to get_followers(), probably save it off in a separate var before sending to function.
        get_followers(ret_val[1])

    counter = counter - 1
