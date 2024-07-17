#!/usr/bin/python3
"""Real definition of a rectangle."""


class Rectangle:
    "Define a Rectangle class"
    def __init__(self, width=0, height=0):
        """Function for access and update attribute"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """property for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width property"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height property """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
