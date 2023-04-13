#!/usr/bin/python3
"""The module contains a script that reads stdin line by line and computes
metrics
"""
import sys


count = 0
while count < 10:
    total_file_size = 0
    dictionary = {}
    for line in sys.stdin:

        splitted_input = line.split()

        if dictionary.get(splitted_input[7]) is None:
            dictionary[splitted_input[7]] = 1
        else:
            dictionary[splitted_input[7]] = (dictionary[splitted_input[7]] + 1)

        count += 1
        total_file_size += int(splitted_input[8])

        if count == 10:
            break

    if count == 10:
        print("File size: {}".format(total_file_size))
        for key, value in sorted(dictionary.items()):
            print("{}: {}".format(key, value))
        count = 0
