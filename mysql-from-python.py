import os
import pymysql

# Get username
username = os.getenv("C9_USER")

# Connect to the database
connection = pymysql.connect(
    host="localhost", user=username, password="", db="Chinook")

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Cloe the connection, regardless of whether the above was sucessful
    connection.close()
