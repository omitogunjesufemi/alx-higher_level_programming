#!/usr/bin/python3
"""This module contains the Base Class of the Project

It manages the id attribute of all classes that inherits form it
to avoid duplicating the same code
"""
import json


class Base:
    """ Base Class
    This class is the base of all other classes in this project.
    It manages the id attribute of all classes that inherits form it
    to avoid duplicating the same code

    Attributes:
     - __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON is one of the standard formats for sharing
        data representation.

        This method is a static method that returns the
        JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        json_str = json.dumps(list_dictionaries)
        return json_str

    @classmethod
    def save_to_file(cls, list_objs):
        """This writes the JSON string representation of list_objs to a file
        """
        instance = cls.__name__
        filename = instance + ".json"

        with open(filename, "w") as json_file:
            if list_objs is None or len(list_objs) == 0:
                json_file.write("[]")
            else:
                new_obj_list = []
                for instance in list_objs:
                    dict_instance = instance.to_dictionary()
                    new_obj_list.append(dict_instance)
                json_string = Base.to_json_string(new_obj_list)
                json_file.write(json_string)
