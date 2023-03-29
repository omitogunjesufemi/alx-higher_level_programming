#!/usr/bin/python3

def safe_print_integer(value):
    try:
        x = int(value)
        y = float(value)
        if x - y == 0:
            print("{:d}".format(x))
            return True
        else:
            return False
    except (ValueError, TypeError):
        return False
