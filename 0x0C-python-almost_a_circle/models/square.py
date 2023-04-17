#!/usr/bin/python3
"""This module contains the Square class
"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """Square Class inherits from Rectangle class
    """
    def __init__(self, size=0, x=0, y=0, id=None):
        """Initialises the Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Square class implementation
        """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x,
                                             self.y, self.width)

    @property
    def size(self):
        """Size attribute if Square class:
        Assigns from width
        """
        return (self.width)

    @size.setter
    def size(self, size):
        """This is a getter for Square size
        """
        self.width = size
