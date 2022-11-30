#!/usr/bin/python3
def remove_char_at(str, n):
    char_array = ""
    i = 0
    while i < len(str):
        if i != n:
            char_array = char_array + str[i]
        i = i + 1
    return char_array
