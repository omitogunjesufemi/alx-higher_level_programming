#!/usr/bin/python3
"""This module contains the Square class
"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """Square Class inherits from Rectangle class

    Attributes:
        size: size of the square
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

    def update(self, *args, **kwargs):
        """Update the Rectangle class
        """
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.size = args[1]
                elif i == 2:
                    self.x = args[2]
                elif i == 3:
                    self.y = args[3]
                else:
                    pass
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """It returns the dictionary representation of a Square

        {id: 0, size: 0, x: 0, y: 0}
        """
        sqr_dict = self.__dict__
        new_sqr_dict = {}

        for key, value in sqr_dict.items():
            if key.startswith("_"):
                key = key.lstrip("_Rectangle__")
                if key == "width":
                    key = "size"
                if key == "height":
                    continue
            new_sqr_dict[key] = value

        return (new_sqr_dict)
