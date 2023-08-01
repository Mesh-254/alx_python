#!/usr/bin/python3
"""  Module Sqaure """


class Square:
    """
    A square class that defines square
    atttributes:
        Private instance attribute: size
    returns:
        private attribute size
    """

    def __init__(self, size=0):
        """
        Constructor method for the Square Class
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the private property size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter"""
        # check if size is integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        # check if size is greater than zero
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the current square area"""
        return (self.__size * self.__size)
