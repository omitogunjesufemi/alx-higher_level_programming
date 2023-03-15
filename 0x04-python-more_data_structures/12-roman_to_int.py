#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not_a_string(roman_string) == 1:
        return 0

    roman_char = {"I": 1, "V": 5, "X": 10,
                  "L": 50, "C": 100, "D": 500, "M": 1000}
    solve_list = []

    for i in range(len(roman_string)):
        solve_list.append(roman_char[roman_string[i]])

        if len(solve_list) >= 2:
            if solve_list[i - 1] < solve_list[i]:
                solve_list[i - 1] = solve_list[i - 1] * (-1)

    return (sum(solve_list))

def not_a_string(string):
    for s in string:
        if s in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            return 1
    return 0
