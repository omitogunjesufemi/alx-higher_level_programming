#!/usr/bin/python3
"""This module contains a function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean) for JSON
serialization of an object
"""
import json


def class_to_json(obj):
    """A function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) for JSON
    serialization of an object
    """
    json_rep = json.dumps(obj.__dict__)
    return json_rep
