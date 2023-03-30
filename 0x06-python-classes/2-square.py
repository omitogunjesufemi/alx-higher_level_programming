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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
