#!/usr/bin/python3
"""
MOdule 1-square
Defines class square with private attributes size
"""


class square:
    """
    class Square definition 
    Args:
    size: size of a side in square
    """

    def __init__(self, size):
        
        """

        initising square
        Attributes:
            size: size of a side of square
        """

        self.__size = size