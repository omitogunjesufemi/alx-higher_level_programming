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
        user="root",
        port=3306,
        passwd="password",
        db="hbtn_0e_0_usa")
    cur = db.cursor()
    count = cur.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    i = 0
    while (i < count):
        print(cur.fetchone())
        i += 1
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
