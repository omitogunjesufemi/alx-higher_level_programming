#!/usr/bin/python3
"""This module inherits from Rectangle which creates a Square class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle
    """
    def __init__(self, size):
        """Initialises the Square class
        """
        BaseGeometry.integer_validator(self, "size", size)
        self.__size = size

    def __str__(self):
        """String representation of the object
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Public instance method that produces area of the shape
        """
        return (self.__size * self.__size)
