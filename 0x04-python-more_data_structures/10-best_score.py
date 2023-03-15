#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(list(a_dictionary.keys())) == 0:
        return None
    largest = (list(a_dictionary.values()))[0]
    best_key = (list(a_dictionary.keys()))[0]

    for key, value in a_dictionary.items():
        if value > largest:
            largest = value
            best_key = key
    return best_key
