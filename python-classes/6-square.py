#!/usr/bin/python3
"""Define a Square class."""


class Square:
    """Document for a Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Document for access and update attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if (not isinstance(position, tuple) or len(position) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """Document for property to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Document Property setter to set new size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Position Getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """Position Setter"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):

            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Document for area of size"""
        return self.__size ** 2

    def my_print(self):
        """Function for print # """
        if self.__size == 0:
            print()
            return None
        else:
            for i in range(self.position[1]):
                print()

            for i in range(self.size):
                for j in range(self.position[0]):
                    print(" ", end="")

                for j in range(self.size):
                    print('#', end="")
                print()
