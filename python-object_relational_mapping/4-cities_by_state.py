#!/usr/bin/python3
""" Python - Object-relational mapping
    task04:
"""
import MySQLdb
import sys


def main():
    """
    Connect to a MySQL server running on localhost at port 3306
    Display the rows of all cities from the database hbtn_0e_4_usa

    Args:
        sys.argv[1] (str): Username for MySQL authentication.
        sys.argv[2] (str): Password for MySQL authentication.
        sys.argv[3] (str): Database name to connect to.
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
    cur.execute(
            "SELECT cities.id, cities.name, states.name \
               FROM cities, states \
              WHERE states.id = cities.state_id \
           ORDER BY cities.id ASC;"
        )

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
