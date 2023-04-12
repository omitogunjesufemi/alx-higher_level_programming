#!/usr/bin/python3
"""This module contains a function that returns the JSON representation of
an object (string)
"""
import json


def to_json_string(my_obj):
    """A function that returns the JSON representation of an object
    """
    json_representation = json.dumps(my_obj)
    return json_representation
