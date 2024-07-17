#!/usr/bin/python3
"""Area of a square"""


class Square:
    """Method returns the current square """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current area"""
        return self.__size ** 2
