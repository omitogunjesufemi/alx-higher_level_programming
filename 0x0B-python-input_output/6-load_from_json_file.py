#!/usr/bin/python3
"""This module contains a function that creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """A function that creates an object from a JSON file
    """
    with open(filename, "r", encoding="utf-8") as f:
        json_rep = f.read()
        return (json.loads(json_rep))
