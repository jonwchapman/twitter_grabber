def add_tweet(val, mydb):
    stmt2 = "INSERT INTO tweet (tweet_id, user_id, parent_tweet, date, time, tweet) VALUES (%s, %s, %s , %s, %s, %s)"

    try:
        cursor = mydb.cursor()
        cursor.execute(stmt2, val)
        mydb.commit()
        return 1

    except:
        return 0
