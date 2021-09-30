#!/usr/bin/python3
"""
Model 2-sqaure
Defines class aquare with atributes size and validates size
"""

class square:
    """
    class Square definition 
    Args:
        size (int): size of a side in square
    """

    def __init__(self, size=0):
        """
        initializes square
        Attributes:
            __size(int): size of square, defaults to 0 if none
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self__size = size