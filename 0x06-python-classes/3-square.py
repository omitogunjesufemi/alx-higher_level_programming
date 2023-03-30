#!/usr/bin/python3
"""This module contains a class Square which defines a square
"""


class Square:
    """Square class which defines a square with a private instance
    attribute with value and type verification

    Attributes:
            __size - prinvate instance attribute
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """A public instance method that returns the current square area
        """
        return self.__size ** 2
