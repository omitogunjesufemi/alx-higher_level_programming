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
        self.__y = y
