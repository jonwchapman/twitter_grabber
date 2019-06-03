
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

