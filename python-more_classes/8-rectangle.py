#!/usr/bin/python3
"""Real definition of a rectangle."""


class Rectangle:
    "Define a Rectangle class"
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Function for access and update attribute"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Function returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Function returns perimetr of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Should print the rectangle with the character #"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""

        for _ in range(self.height):
            rectangle_str += str(self.print_symbol) * self.width + "\n"
        return rectangle_str.rstrip("\n")

    def __repr__(self):
        """should return a string representation of the rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Remove class instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to return the rectangle with the larger area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.width * rect_1.height
        area_2 = rect_2.width * rect_2.height

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2
