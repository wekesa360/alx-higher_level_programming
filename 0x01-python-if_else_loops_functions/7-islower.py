#!/usr/bin/python3
def islower(c):
    """Check for lowercase characters."""
    c = ord(c)
    if c >= 97 and c < 123:
        return True
    else:
        return False