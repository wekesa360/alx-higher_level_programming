#!/usr/bin/python3
"""
Module 3-square
Defines class square with attribute size and public attribute area
"""

class Square:
    """
    class Square definition
    Args:
        size (int): size of a side in square
    Functions:
        __init__(self, size)
        area(self)
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise ValueError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size
    def area(self):
        """
        Claculates the area of square 
        Returns
            area
        """
        return (self.__zize)**2
