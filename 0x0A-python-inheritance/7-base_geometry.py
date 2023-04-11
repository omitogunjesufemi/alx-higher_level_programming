#!/usr/bin/python3
"""This module is creates an empty class:
   BaseGeometry
"""


class BaseGeometry:
    """BaseGeometry is an empty class
    """
    def area(self):
        """Public instance method that raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method for validating value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
