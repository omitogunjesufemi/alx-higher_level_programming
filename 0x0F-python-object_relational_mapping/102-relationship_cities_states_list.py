#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_06_usa
   It takes 3 arguments: mysql username, mysql password, database name
   It uses the SQLAlchemy module. It is safe from MySQL injections
"""
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(user, passwd, db))
    Session = sessionmaker(engine)
    Base.metadata.create_all(engine)
    session = Session()

    cities = session.query(City).all()
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
