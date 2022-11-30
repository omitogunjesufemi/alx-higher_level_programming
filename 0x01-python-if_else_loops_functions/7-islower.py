"""
* islower function
* Returns True if lower, and false if otherwise
"""
def islower(c):
    ascii_int = ord(c)
    if ascii_int in range(97, 112):
        return True
    else:
        return False
