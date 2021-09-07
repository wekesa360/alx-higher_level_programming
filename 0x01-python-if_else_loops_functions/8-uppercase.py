#!/usr/bin/python3
def islower(c):
    """Check for uppercase characters."""
    c = ord(c)
    if c >= 65 and c < 91:
        return True 
    else:
        return False