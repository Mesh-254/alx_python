#!/usr/bin/python3
"""Rectangle Module"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class rectangle """

    def __init__(self, width, height):
        """instantiation method"""
        # validated by integer_validator from BaseGeometry
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        # creation of private attributes
        self.__width = width
        self.__height = height
