#!/usr/bin/python3
"""This module contains the class definition of State and an instance
   Base = declarative_base()

   State class:
      Inherits from Base
      Links to MySQL table states

   SQLAlchemy module is used here
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """State class:
    - Inherits from Base
    - Links to MySQL table states
    - Class attribute id that represents a column of an auto-generated,
    unique integer, can't be null and is a primary key
    - Class attribute name that represents a column of a string with
    maximum 128 characters and can't be null
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")

    def __init__(self, name):
        """Initializes the State Class"""
        self.name = name
