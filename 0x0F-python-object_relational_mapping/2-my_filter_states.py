#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa when name match
   It takes 4 arguments: mysql username, mysql password, database name, name
   It uses the MySQLdb module
"""
import MySQLdb
import sys


def main():
    """The entry point of the program"""
    db = MySQLdb.connect(
        host="localhost",
        user=f"{sys.argv[1]}",
        passwd=f"{sys.argv[2]}",
        db=f"{sys.argv[3]}",
        port=3306)
    cur = db.cursor()
    query = """SELECT * FROM states
    WHERE states.name = \'{}\'
    ORDER BY states.id ASC""".format(sys.argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
