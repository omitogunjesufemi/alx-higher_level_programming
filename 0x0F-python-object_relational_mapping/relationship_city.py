#!/usr/bin/python3
"""This module contains the class definition of City and an instance
   Base = declarative_base()

   City class:
      Inherits from Base
      Links to MySQL table states

   SQLAlchemy module is used here
"""
from relationship_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """City class:
    - Inherits from Base
    - Links to MySQL table states
    - Class attribute id that represents a column of an auto-generated,
    unique integer, can't be null and is a primary key
    - Class attribute name that represents a column of a string with
    maximum 128 characters and can't be null
    - Class attribute state_id that represents a column of an integer,
    can't be null and is a foreign key to states.id
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    def __init__(self, name):
        """Initialises City Class"""
        self.name = name
