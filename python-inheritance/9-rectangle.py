#!/usr/bin/python3
"""Geometry module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Test case"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Function returns area"""
        return self.__width * self.__height

    def __str__(self):
        """Str"""
        return f"[Rectangle] {self.__width}/{self.__height}"
