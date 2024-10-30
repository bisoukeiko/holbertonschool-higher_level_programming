#!/usr/bin/python3
""" Python - Object-relational mapping
    task05:
"""
import MySQLdb
import sys


def main():
    """
    Connect to a MySQL server running on localhost at port 3306
    Takes in the name of a state as an argument and displays all cities name
    in the states table from the database hbtn_0e_4_usa

    Args:
        sys.argv[1] (str): Username for MySQL authentication.
        sys.argv[2] (str): Password for MySQL authentication.
        sys.argv[3] (str): Database name to connect to.
        sys.argv[4] (str): City name to be searched.
    """
    db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3],
                charset="utf8"
            )

    cur = db.cursor()

    parameter = (sys.argv[4],)

    query = "SELECT cities.name \
               FROM cities, states \
              WHERE states.id = cities.state_id \
                AND  BINARY states.name = %s \
           ORDER BY cities.id ASC;"

    cur.execute(query, parameter)

    query_rows = cur.fetchall()

    index = 0
    for row in query_rows:
        if index != (len(query_rows) - 1):
            print(row[0], end=", ")
        else:
            print(row[0], end="")
        index += 1

    print()

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
