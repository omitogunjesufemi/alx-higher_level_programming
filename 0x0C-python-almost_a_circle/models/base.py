#!/usr/bin/python3
"""This module contains the Base Class of the Project

It manages the id attribute of all classes that inherits form it
to avoid duplicating the same code
"""
import json
import csv
import os
import turtle


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

        with open(filename, "w", encoding="utf-8") as json_file:
            if list_objs is None or len(list_objs) == 0:
                json_file.write("[]")
            else:
                new_obj_list = []
                for instance in list_objs:
                    dict_instance = instance.to_dictionary()
                    new_obj_list.append(dict_instance)
                json_string = Base.to_json_string(new_obj_list)
                json_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """It returns the list of the JSON string representation

        json_string - is a string representing a list of dictionaries

        If json_string is None or empty, return an empty list
        Otherwise, return the list represented by json_string
        """
        if json_string == "" or json_string is None:
            return []

        json_rep = json.loads(json_string)
        return (json_rep)

    @classmethod
    def create(cls, **dictionary):
        """This returns an instance with all attributes already set
        """
        instance = cls(1, 1)
        instance.update(**dictionary)
        return (instance)

    @classmethod
    def load_from_file(cls):
        """This returns a list of instances from a file

        The file name must be: <Class name>.json - example Rectangle.json

        If the file doesn't exist, return an empty list
        Othwerwise return a list of instances - the type of these instances
        depends on cls - current class using the method
        """
        filename = cls.__name__ + ".json"
        instance_list = []

        if os.path.exists(filename) is False:
            return instance_list

        with open(filename, "r", encoding="utf-8") as from_file:
            json_string = from_file.read()
            dict_json = Base.from_json_string(json_string.strip('\n'))

        for item in dict_json:
            instance_list.append(cls.create(**item))

        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """It serialises into csv format
        """
        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="", encoding="utf-8") as csv_file:
            if list_objs is None or len(list_objs) == 0:
                csv_writer = csv.writer(csv_file, delimiter=',')
                csv_writer.writerow([])
            else:
                instance_list = []
                csv_writer = csv.writer(csv_file, delimiter=',')
                for obj in list_objs:
                    instance_list.append(obj.to_dictionary())
                for instance in instance_list:
                    values = []
                    for key, value in instance.items():
                        values.append(int(value))
                    csv_writer.writerow(values)

    @classmethod
    def load_from_file_csv(cls):
        """This deserialises from csv format
        """
        filename = cls.__name__ + ".csv"
        instance_list = []

        if os.path.exists(filename) is False:
            return instance_list

        with open(filename, "r", newline="", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                row = tuple(map(int, row))
                instance = cls(1, 1)
                instance.update(*row)
                instance_list.append(instance)

        return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """This opens a window and draws all the Rectangles and Squares
        """
        screen = turtle.getscreen()
        base_shape = turtle.Turtle()
        base_shape.home()

        for rectangle in list_rectangles:
            base_shape.color("red", "blue")
            base_shape.penup()
            base_shape.pendown()
            base_shape.begin_fill()
            base_shape.forward(rectangle.width)
            base_shape.right(90)
            base_shape.forward(rectangle.height)
            base_shape.right(90)
            base_shape.forward(rectangle.width)
            base_shape.right(90)
            base_shape.forward(rectangle.height)
            base_shape.end_fill()
            base_shape.penup()
            base_shape.goto(10, 10)

        base_shape.home()
        base_shape.goto(-30, -30)
        for square in list_squares:
            base_shape.color("yellow", "green")
            base_shape.penup()
            base_shape.pendown()
            base_shape.begin_fill()
            base_shape.forward(square.width)
            base_shape.right(90)
            base_shape.forward(square.height)
            base_shape.right(90)
            base_shape.forward(square.width)
            base_shape.right(90)
            base_shape.forward(square.height)
            base_shape.end_fill()
            base_shape.penup()
            base_shape.goto(-30, -30)
