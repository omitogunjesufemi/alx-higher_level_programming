#!/usr/bin/python3
"""This module contains a function that inserts a line of text to a
file, after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """A function that inserts a line of text to a file, after each
    line containing a specific string
    """

    with open(filename, "r+", encoding="utf-8") as f:
        f_content = list(f)
        for i in range(len(f_content)):
            line = f_content[i]
            position = line.find(search_string)
            if position >= 0:
                line += new_string
                f_content[i] = line

        f.truncate(0)
        for line in f_content:
            f.write(line)
