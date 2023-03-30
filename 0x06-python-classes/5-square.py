#!/usr/bin/python3
"""This module contains a class Square which defines a square
"""


class Square:
    """Square class which defines a square with a private instance
    attribute with value and type verification

    Attributes:
            __size - prinvate instance attribute
            area - returns the current square area
            my_print - prints in stdout the square with the character #
    """
    def __init__(self, size=0):
        """This initializes the class with a size of type int

        Args:
            size (int): should be an integer, also not less than zero
        """
        self.size = size

    @property
    def size(self):
        """This returns the size of the square
        Returns: int
        """
        return self.__size

    @size.setter
    def size(self, value):
        """This sets the size with an integer value

        Args:
            value (int) - should be an integer, also not less than zero

        ValueError - when the size is less than 0
        TypeError - when the size is not an integer
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """A public instance method that returns the current
        square area

        Returns: int
        """
        return self.__size ** 2

    def my_print(self):
        """A public instance method that prints in stdout the square
        with the character #, and prints an empty line when size is zero
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
