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
        # rows = [("bob", 21, "1990-02-06 23:04:56"),
        #         ("jim", 56, "1955-05-09 13:12:45"),
        #         ("fred", 100, "1911-09-12 01:01:01")]
        list_of_names = ["fred", "Fred"]
        # prepare a string with same number of placeholders as in list_of_names
        format_strings = ",".join(["%s"]*len(list_of_names))
        cursor.execute(
            "DELETE FROM Friends WHERE name in ({});"
            .format(format_strings), list_of_names)
        connection.commit()
        for row in cursor:
            print(row)
finally:
    # Cloe the connection, regardless of whether the above was sucessful
    connection.close()
