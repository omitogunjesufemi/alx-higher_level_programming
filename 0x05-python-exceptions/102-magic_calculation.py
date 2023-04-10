#!/usr/bin/python3
"""This module is a replication of the magic calculation from
a Python Bytecode
"""


def magic_calculation(a, b):
    """Magic calculation
    """
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += (a ** b) / i
        except Exception:
            result = a + b
            break

    return result
