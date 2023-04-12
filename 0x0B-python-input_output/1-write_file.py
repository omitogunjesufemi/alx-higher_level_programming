#!/usr/bin/python3
"""This module contains a function that writes a string to a text file and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file (UTF8) and returns
    the number of characters written:

    It creates the file if doesn’t exist.
    It overwrites the content of the file if it already exists.
    """
    with open(filename, "w", encoding="utf-8") as f:
        character_count = f.write(text)
        return character_count - 1
