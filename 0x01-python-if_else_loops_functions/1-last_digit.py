#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if (number < 0):
    last_digit = (number * -1) % 10
result_str = f"Last digit of {number} is {last_digit}"

if last_digit > 5:
    print(result_str, f"and is greater than 5")
elif last_digit == 0:
    print(result_str, f"and is 0")
elif last_digit < 6 and last_digit != 0:
    print(result_str, f"and is less than 6 and not 0")
