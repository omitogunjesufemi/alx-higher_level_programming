#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys = []
    for key, val in a_dictionary.items():
        if val == value:
            keys.append(key)

    for key in keys:
        a_dictionary.pop(key)
    return a_dictionary
