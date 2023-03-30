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
        self.size = size

    @property
    def size(self):
        """Attr: size of the square
        Returns: int
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """A public instance method that returns the current square area
        """
        return self.__size ** 2

    def __lt__(self, other):
        """This function checks if the instantiated object is less than
        the other object being compared to
        """
        return self.area() < other.area()

    def __gt__(self, other):
        """This function checks if the instantiated object is
        greater than the other object being compared to
        """
        return self.area() > other.area()

    def __le__(self, other):
        """This function checks if the instantiated object is less than
         or equals to the other object being compared to
        """
        return self.area() <= other.area()

    def __ge__(self, other):
        """This function checks if the instantiated object is greater
        than or equals to the other object being compared to
        """
        return self.area() >= other.area()

    def __eq__(self, other):
        """This function checks if the instantiated object is equals
        to the other object being compared to
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """This function checks if the instantiated object is not equal
        to the other object being compared to
        """
        return self.area() != other.area()
