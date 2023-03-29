#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        x = fct(*args)
        return x
    except Exception as exc:
        print("Exception:", exc, file=sys.stderr)
        return None
