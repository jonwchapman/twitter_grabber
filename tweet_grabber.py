import twint
from add_tweet import add_tweet
from add_user import add_user
from db_connection import db_connection
import mysql.connector
from os import system, name


c = twint.Config()
c.Limit = 100
c.Hide_output = True
c.Search = "vax"
c.Store_object = True
c.Resume = 1134879742304276480

user_added = 0
user_present = 0
tweet_added = 0
tweet_present = 0
progress = 0
loops = 2
limit = c.Limit * loops

mydb = db_connection()

while loops >= 1:
    try:
        twint.run.Search(c)
    except:
        # TODO: Figure out the error
        print("UNDETERMINED ERROR")

    tweets = twint.output.tweets_object

    for tweet in tweets:
        progress = 1 + progress
        print(str(progress) + "/" + str(limit))
        single_tweet = tweet
        tweet_id = single_tweet.id
        user_id = single_tweet.user_id
        tweet_text = single_tweet.tweet
        date = single_tweet.datestamp
        time = single_tweet.timestamp
        user_name = single_tweet.username

        try:
            parent_tweet = single_tweet.user_rt
        except:
            parent_tweet = 0

        val1 = (user_id, user_name)
        user_added_par = add_user(user_id, user_name, mydb)
        user_added = user_added + user_added_par

        val2 = (tweet_id, user_id, parent_tweet, date, time, tweet_text)
        tweet_added_par = add_tweet(val2, mydb)
        tweet_added = tweet_added + tweet_added_par

        print(str(user_added) + " users added.")
        print(str(tweet_added) + " tweets added.")

    tweets.clear()
    loops = loops - 1



