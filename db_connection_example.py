import mysql.connector


def db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="user",
        passwd="password",
        database="twitter"
    )
    return mydb
