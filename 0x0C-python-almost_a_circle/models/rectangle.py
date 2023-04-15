#!/usr/bin/python3
"""This module contains the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class that inherits from Base

    Attributes:
        __width
        __height
        __x
        __y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle class
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """This is a getter for the private instance attribute: width
        """
        return (self.__width)

    @width.setter
    def width(self, width):
        """This is a setter for the private instance attribute: width
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """This is a getter for the private instance attribute: height
        """
        return (self.__height)

    @height.setter
    def height(self, height):
        """This is a setter for the private instance attribute: height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """This is a getter for the private instance attribute: x
        """
        return (self.__x)

    @x.setter
    def x(self, x):
        """This is a setter for the private instance attribute: x
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """This is a getter for the private instance attribute: y
        """
        return (self.__y)

    @y.setter
    def y(self, y):
        """This is a setter for the private instance attribute: y
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """This returns the area value of the Rectangle instance
        """
        return (self.__width * self.__height)

    def display(self):
        """This prints in the stdout the Rectangle instance with
        the character #
        """
        for row in range(self.__height):
