#!/usr/bin/python3

"""This module creates a class for Rectangle class that defines
a rectangle

Attributes:
    width - private instance attribute
    height - private instance attribute
"""


class Rectangle:
    """Rectangle class defines a rectangle

    Attributes:
        width - private instance attribute
        height - private instance attribute

    It is an empty class
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width to a particular value

                value (int)

        TypeError: width must be an integer
        ValueError: width must be >= 0
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height to a particular value

                value (int)

        TypeError: height must be an integer
        ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """This returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
