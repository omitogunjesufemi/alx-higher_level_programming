#!/usr/bin/python3
"""
This module is about a class Square that defines a square

Todo:
    * Instantiate the class with size with no type or value verification
"""


class Square:
    """Square class that defines a square by a private instance
    attribute of size, which is instantiated with no type or value
    verification

    Attribute:
            __size - private attribute
    """
    def __init__(self, size=0):
        self.__size = size
