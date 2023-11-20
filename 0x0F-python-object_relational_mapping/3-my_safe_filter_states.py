#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa when name match
   It takes 4 arguments: mysql username, mysql password, database name, name
   It uses the MySQLdb module. It is safe from MySQL injections
"""
import MySQLdb
import sys


def main():
    """The entry point of the script """
    db = MySQLdb.connect(
        host="localhost",
        user=f"{sys.argv[1]}",
        passwd=f"{sys.argv[2]}",
        port=3306,
        db=f"{sys.argv[3]}")

    cur = db.cursor()

    query = """SELECT * FROM states
    WHERE states.name = %s
    ORDER BY states.id ASC"""

    try:
        cur.execute(query, (sys.argv[4], ))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        pass


if __name__ == "__main__":
    main()
