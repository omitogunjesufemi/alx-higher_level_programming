#!/usr/bin/python3

"""This import math function into this module"""
import math

"""
This is a module for MagicClass ByteCode -> #Python5
"""

class MagicClass:
    """This MagicClass is defined to create a circle with a particular radius
    and get the area and circumference of the circle

    Attribute:
            __radius: A private instance attribute
    """

    def __init__(self, radius):
        """This initialises the MagicClass with a radius value which is an
        int or fliat
        """
        self.__radius = radius

    @radius.setter
    def radius(self, radius):
        """This setter property sets the value of radius to an int or float

        TypeError:
               radius must be a number
        """
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    @property
    def radius(self):
        """This property returns the value of the radius of the MagicClass
        """
        return self.__radius

    def area(self):
        """This returns the area of the magic class
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """This returns the circumference of the magic class
        """
        return 2 * math.pi * (self.__radius)
