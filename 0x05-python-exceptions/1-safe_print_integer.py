#!/usr/bin/python3

def safe_print_integer(value):
    try:
        x = int(value)
        print("{:d}".format(x))
        return True
    except (ValueError, TypeError):
        return False
