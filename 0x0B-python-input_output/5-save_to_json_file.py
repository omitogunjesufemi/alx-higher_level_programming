#!/usr/bin/python3
"""This module contains a function that writes an Object to a text file using
JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """A function that writes an Object to a text file using JSON
    """
    json_rep = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json_rep)
