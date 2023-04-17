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
            if self.__y != 0 and row == 0:
                print("\n" * self.__y, end="")
            for col in range(self.__width):
                if self.__x != 0 and col == 0:
                    print(" " * self.__x, end="")
                if col == self.__width - 1:
                    print("#", end="\n")
                else:
                    print("#", end="")

    def __str__(self):
        """Rectangle class implementation
        """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.x,
                                                self.y, self.width,
                                                self.height)

    def update(self, *args, **kwargs):
        """Update the Rectangle class
        """
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                elif i == 2:
                    self.height = args[2]
                elif i == 3:
                    self.x = args[3]
                elif i == 4:
                    self.y = args[4]
                else:
                    pass
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
