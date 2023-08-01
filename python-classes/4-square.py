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
        """attribute instantiation"""

        self.__size = size

    @property
    def size(self):
        """Returns private property size"""

        return self.__size

    @size.setter
    def size(self, value):
        """property setter:
        Sets size to a value
        """
        # check if value if integer type
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        # check if value is greater than 0
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """returns the current square area"""

        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""
        for row in range(self.__size):
            for column in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print(end=("\n"))
