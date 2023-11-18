#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_06_usa
   It takes 4 arguments: mysql username, mysql password, db name, state_name
   It uses the SQLAlchemy module - SQL Injection Free
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(user, passwd, db))
    Session = sessionmaker(engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
