#!/usr/bin/python3

import MySQLdb
import sys


def lists_states(username, password, database_name):
    try:

        db = MySQLdb.connect(
                host="localhost",
                user=username,
                passwd=password,
                db=database_name,
                port=3306
                )

        # Create a cursor object to execute queries
        cursor = db.cursor()

        # Execute the query
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

        # Get all the rows
        states = cursor.fetchall()

        # Display results
        for state in states:
            print(state)

        # Close connection
        cursor.close()
        db.close()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    # Check if the script is executed directly
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    lists_states(username, password, database_name)
