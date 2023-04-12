#!/usr/bin/python3
"""
"""


def append_write(filename="", text=""):
    """
    """
    with open(filename, "a", encoding="utf-8") as f:
        character_count = f.write(text)
        if text == "":
            return 0
        return character_count
