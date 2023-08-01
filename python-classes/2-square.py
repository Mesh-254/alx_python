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
        # check if size is integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # check if size is greater than zero
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ returns the current square area"""
        return (self.__size * self.__size)
