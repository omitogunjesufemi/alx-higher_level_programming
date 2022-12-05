#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_a = (0, None)
    length = len(sentence)

    if length < 1:
        return tuple_a
    else:
        first_char = sentence[0]
        tuple_a = length, first_char
    return tuple_a
