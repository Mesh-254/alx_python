#!/usr/bin/python3

"""class rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init method to initialize objects"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # getter method to get the properties of width
    @property
    def width(self):
        """getter method to get the properties of width"""
        return self.__width

    # setting new values for width and updating it in object
    @width.setter
    def width(self, width):
        """setter method to change the value 'width' using an object"""
        self.__width = width

    # getter method to get the properties of height
    @property
    def height(self):
        """getter method to get the properties of height"""
        return self.__height

    # setting new values for height and updating it in object
    @ height.setter
    def height(self, height):
        """setter method to change the value 'height' using an object"""
        self.__height = height

    # getter method to get the properties of x
    @property
    def x(self):
        """getter method to get the properties of x"""
        return self.__x

    # setting new values for x and updating it in object
    @x.setter
    def x(self, x):
        """setter method to change the value 'x' using an object"""
        self.__x = x

    # getter method to get the properties of y
    @property
    def y(self):
        """getter method to get the properties of y"""
        return self.__y

    # setting new values for y and updating it in object
    @y.setter
    def x(self, y):
        """setter method to change the value 'y' using an object"""
        self.__y = y
