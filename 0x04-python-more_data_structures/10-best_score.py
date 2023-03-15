#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    largest = (list(a_dictionary.values()))[0]
    best_key = ""

    for key, value in a_dictionary.items():
        if value > largest:
            largest = value
            best_key = key
    return best_key
