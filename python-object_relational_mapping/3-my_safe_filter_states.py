#!/usr/bin/python3
""" Python - Object-relational mapping
    task03:
"""
import MySQLdb
import sys


def main():
    """
    Connect to a MySQL server running on localhost at port 3306
    Takes in an argument and displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument with safe from

    Args:
        sys.argv[1] (str): Username for MySQL authentication.
        sys.argv[2] (str): Password for MySQL authentication.
        sys.argv[3] (str): Database name to connect to.
        sys.argv[4] (str): State name to be searched.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    cur = db.cursor()

    parameter = (sys.argv[4],)

    query = "SELECT id, name \
                   FROM states \
                  WHERE BINARY name = %s \
               ORDER BY id ASC;"

    cur.execute(query, parameter)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
