#!/usr/bin/python3
def no_c(my_string):
    str_len = len(my_string)
    chck = "Cc"
    new_str = ""

    for c in my_string:
        if c not in chck:
            new_str += c
    return (new_str)
