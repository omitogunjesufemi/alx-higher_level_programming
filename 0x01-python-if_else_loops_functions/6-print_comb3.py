#!/usr/bin/python3
x, y = 0, 0
while x < 10:
    while y < 10:
        if x != y:
            print('{:d}{:d}'.format(x, y), end="")
        y = y + 1
    x = x + 1
    y = x
