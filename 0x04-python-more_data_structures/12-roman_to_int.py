#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_char = {"I": 1, "V": 5, "X": 10,
                  "L": 50, "C": 100, "D": 500, "M": 1000}
    solve_list = []

    for i in range(len(roman_string)):
        solve_list.append(roman_char[roman_string[i]])

        if len(solve_list) >= 2:
            if solve_list[i - 1] < solve_list[i]:
                solve_list[i - 1] = solve_list[i - 1] * (-1)

    return (sum(solve_list))
