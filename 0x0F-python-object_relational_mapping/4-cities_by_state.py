#!/usr/bin/python3
"""This script lists all cities from the database hbtn_0e_4_usa
   It takes 3 arguments: mysql username, mysql password, database name
   It uses the MySQLdb module
"""
import MySQLdb
import sys


def main():
    """Entry point of the script"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )

    cur = db.cursor()
    query = """SELECT cities.id, cities.name, states.name
    FROM cities, states WHERE cities.state_id = states.id
    ORDER BY cities.id ASC"""
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
