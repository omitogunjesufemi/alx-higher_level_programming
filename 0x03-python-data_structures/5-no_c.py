#!/usr/bin/python3

def no_c(my_string):
    str_list = ""
    for s in my_string:
        if s == "c" or s == "C":
            continue
        str_list = str_list + s
    return str_list
