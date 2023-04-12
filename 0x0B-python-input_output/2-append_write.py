#!/usr/bin/python3
"""This module contains a function that appends a string at the end of a text
file and returns the number of characters added
"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file and returns
    the number of characters added:

    File is created if it doesn't exist
    """
    with open(filename, "a", encoding="utf-8") as f:
        character_count = f.write(text)
        if text == "":
            return 0
        return character_count
