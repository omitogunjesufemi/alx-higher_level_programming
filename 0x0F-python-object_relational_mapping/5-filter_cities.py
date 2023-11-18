#!/usr/bin/python3
"""This script lists all cities from the database hbtn_0e_0_usa when state name
   match. It takes 4 arguments: mysql username, mysql password, database name,
   name. It uses the MySQLdb module. It is safe from MySQL injections
"""
import MySQLdb
import sys


def main():
    """Entry point of the script"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=db_name,
        port=3306,
        host="localhost"
    )
    cur = db.cursor()
    query = """SELECT cities.name FROM cities, states
    WHERE cities.state_id = states.id
    AND states.name = %s
    ORDER BY cities.id ASC"""
    count = cur.execute(query, (state_name, ))
    rows = cur.fetchall()

    i = 0
    for row in rows:
        if i == count - 1:
            print(row[0])
        else:
            print(row[0], end=", ")
        i += 1

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
