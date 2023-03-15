#!/usr/bin/python3

def uniq_add(my_list=[]):
    if len(my_list) <= 0:
        return 0

    return (sum(set(my_list)))
