#!/usr/bin/python3
"""
This module creates a class Square that defines a square
"""


class Square:
    """Square class that defines a square that has a private
    instance attribute with value or type verification

    Attribute:
            __size - private attribute
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """int: size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
