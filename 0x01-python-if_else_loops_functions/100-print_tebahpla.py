#!/usr/bin/python3
for ascii_int in reversed(range(65, 91)):
    if ascii_int % 2 == 0:
        ascii_int = ascii_int + 32
    print('{:c}'.format(ascii_int), end="")
