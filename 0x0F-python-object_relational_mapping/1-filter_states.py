#!/usr/bin/python3
"""This module lists all states with a name starting with N from the database
"""
import MySQLdb
import sys


def main():
    """Entry point for the module """
    db = MySQLdb.connect(
        host="localhost",
        user=f"{sys.argv[1]}",
        passwd=f"{sys.argv[2]}",
        port=3306,
        db=f"{sys.argv[3]}")
    cur = db.cursor()
    query = """
    SELECT * FROM states
    WHERE BINARY states.name LIKE N'N%'
    ORDER BY states.id ASC
    """
    try:
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        pass

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
