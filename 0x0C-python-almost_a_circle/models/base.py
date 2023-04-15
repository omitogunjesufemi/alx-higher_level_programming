#!/usr/bin/python3
"""This module contains the Base Class of the Project

It manages the id attribute of all classes that inherits form it
to avoid duplicating the same code
"""


class Base:
    """ Base Class
    This class is the base of all other classes in this project.
    It manages the id attribute of all classes that inherits form it
    to avoid duplicating the same code

    Attributes:
     - __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
