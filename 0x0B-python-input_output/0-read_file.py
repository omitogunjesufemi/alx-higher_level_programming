#!/usr/bin/python3
"""This module contains a function that read a text file with a UTF-8
encoding and prints it to stdout
"""


def read_file(filename=""):
    """A function that read a text file with a UTF-8 encoding algorithm
    and pirnts it to stdout:

    The with statement is used in this function to open the file

    This function does not manage file permission or other exceptions
    """
    with open(filename, "r", encoding="utf-8") as a_file:
        file_content = a_file.read()
        if file_content != "":
            print(file_content.strip("\n"))
