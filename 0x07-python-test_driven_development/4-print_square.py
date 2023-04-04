#!/usr/bin/python3

def print_square(size):
    """
    Prints a square based on size
    """
    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        size = int(size)

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
