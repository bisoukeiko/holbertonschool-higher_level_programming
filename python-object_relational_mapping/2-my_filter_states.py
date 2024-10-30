#!/usr/bin/python3
""" task02:
    takes in an argument and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys


def main():
    """
    Connect to a MySQL server running on localhost at port 3306
    Takes in an argument and displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument

    Args:
        sys.argv[1] (str): Username for MySQL authentication.
        sys.argv[2] (str): Password for MySQL authentication.
        sys.argv[3] (str): Database name to connect to.
        sys.argv[4] (str): State name to be searched.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    cur = db.cursor()

    state_name = sys.argv[4]

    cur.execute("SELECT id, name \
                   FROM states \
                  WHERE name = '{}' \
               ORDER BY id ASC;".format(state_name))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
