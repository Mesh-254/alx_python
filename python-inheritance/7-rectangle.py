#!/usr/bin/python3
"""Rectangle module"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry """

    def __init__(self, width, height):
        """Instantiation method"""

        # validation of width and height values
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Instantiation of private attributes
        self.__width = width
        self.__height = height

    def area(self):
        """Returnns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string representation"""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
