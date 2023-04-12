#!/usr/bin/python3
"""This module contains a Student class that defines a student by name and age.
"""


class Student:
    """Student class the defines a student by:

    Attributes:
        => first_name
        => last_name
        => age

    Method:
        => to_json
    """

    def __init__(self, first_name, last_name, age):
        """This initializes the class with the attributes:

        Attributes:
            => first_name
            => last_name
            => age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
