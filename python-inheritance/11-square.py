#!/usr/bin/python3
"""Square Class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define Square size"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """for area"""
        return self.__size * self.__size

    def __str__(self):
        """str"""
        c = __class__.__name__
        return ("[{}] {}/{}".format(c, self.__size, self.__size))
