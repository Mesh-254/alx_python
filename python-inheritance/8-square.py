#!/usr/bin/python
"""Square module"""

Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """class square that inherits from rectangle"""

    def __init__(self, size):
        """Instantiation method"""
        super().__init__(size, size)
        # validate input type is integer
        self.integer_validator("size", size)

        self.__width = size
        self.__height = size

    def area(self):
        """Function to return area of square"""
        return self.__width * self.__height
