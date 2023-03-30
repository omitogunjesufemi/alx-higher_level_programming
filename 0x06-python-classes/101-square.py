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
    def __init__(self, size=0, position=(0, 0)):
        """This initializes the class with a size of type int

        Args:
            size (int): should be an integer, also not less than zero
            position (tuple): must be a tuple of 2 positive integers
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """This returns the private instance attribute => position

        Returns: a tuple of two integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """This sets the private instance attribute => position to a
        tuple of 2 positive integers

        Args:
            value (tuple) - must be a tuple of 2 positive integers

        TypeError - position must be a tuple of 2 positive integers
        """
        if type(value) is tuple and len(value) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
            if i == 0 and self.__position[1] > 0:
                for x in range(self.__position[1]):
                    print()
            for j in range(self.__size):
                if j == 0 and self.__position[0] > 0:
                    print(" " * self.__position[0], end="")
                print("#", end="")

                if j == self.__size - 1 and i != self.__size - 1:
                    print()


    def __str__(self):
        self.my_print()
        return ''
