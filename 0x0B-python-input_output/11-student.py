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

    def to_json(self, attrs=None):
        """This retrieves a dictionary representation of a Student instance

        attrs: is a list of strings, only attribute names contained
        in this list must be retrieved
        """

        my_attrs = list(self.__dict__.keys())

        class_dict = {}

        if attrs is None or my_attrs == attrs:
            return self.__dict__

        for attr in my_attrs:
            if attr in attrs:
                class_dict[attr] = self.__dict__[attr]

        return class_dict

    def reload_from_json(self, json):
        """This replaces all attributes of the Student instance
        """
        for key, value in json.items():
            self.__dict__[key] = value
