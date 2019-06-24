from db_connection import db_connection


def add_follower(follower_id, followee_id):
    mydb = db_connection()
    print("Inserting Follower relationship")
    print("follower " + follower_id)
    print("followee " + followee_id)
    stmt1 = "INSERT INTO follow (follower_id, followee_id) VALUES (%s, %s)"

    try:
        cursor = mydb.cursor()
        cursor.execute(stmt1, (follower_id, followee_id))
        mydb.commit()
    except:
        print("Exception adding Follower Relationship")

    return 1
