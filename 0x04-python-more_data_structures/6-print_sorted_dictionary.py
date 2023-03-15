#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())

    if len(keys) > 0:
        keys = sorted(keys)
        for key in keys:
            print("{}: {}".format(key, a_dictionary[key]), end="\n")
