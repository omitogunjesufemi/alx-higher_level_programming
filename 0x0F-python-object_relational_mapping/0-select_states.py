#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa
   It takes 3 arguments: mysql username, mysql password & database name
   It uses the MySQLdb module
"""
import MySQLdb
import sys


def main():
    """This prevents the module from executing when imported as a module
    """
    db = MySQLdb.connect(
        host="localhost",
        user=f"{sys.argv[1]}",
        port=3306,
        passwd=f"{sys.argv[2]}",
        db=f"{sys.argv[3]}")
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
