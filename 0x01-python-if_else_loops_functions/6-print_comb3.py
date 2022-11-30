#!/usr/bin/python3
x, y = 0, 0
while x < 10:
    while y < 10:
        if x != y and (x != 8 or y != 9):
            print('{:d}{:d}, '.format(x, y), end="")
        elif x == 8 and y == 9:
            print('{:d}{:d}'.format(x, y), end="\n")
        y = y + 1
    x = x + 1
    y = x
