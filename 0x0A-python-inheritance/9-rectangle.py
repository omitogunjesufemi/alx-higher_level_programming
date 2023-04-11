#!/usr/bin/python3
"""This module inherits from BaseGeometry which creates a Rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """Initialises the Rectangle class
        """
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height

    def __str__(self):
        """String representation of the object
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Public instance method that raises an Exception
        """
        return (self.__width * self.__height)
