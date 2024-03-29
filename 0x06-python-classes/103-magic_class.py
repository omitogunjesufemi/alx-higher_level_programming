#!/usr/bin/python3
"""MagicClass ByteCode -> #Python5

This module handles and creates the Magic class which takes a radius value to
calculate the area and circumference of a circle.

Todo:
    * Instantiate the class with radius with verification if it is float or int
Arguments:
    * A private instance field: radius
    * A private instance method: area
    * A private instance method: circumference
"""

import math


class MagicClass:
    """This MagicClass is defined to create a circle with a particular radius
    and get the area and circumference of the circle

    Attribute:
            __radius: A private instance attribute
    """

    def __init__(self, radius=0):
        """This initialises the MagicClass with a radius value which is an
        int or fliat
        """
        self.radius = radius

    @property
    def radius(self):
        """This property returns the value of the radius of the MagicClass
        """
        return self.__radius

    @radius.setter
    def radius(self, radius):
        """This setter property sets the value of radius to an int or float

        TypeError:
               radius must be a number
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """This returns the area of the magic class
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """This returns the circumference of the magic class
        """
        return 2 * math.pi * (self.__radius)
