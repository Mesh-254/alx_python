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
    def get_width(self):
        """getter method to get the properties of width"""
        return self.__width

    # setting new values for width and updating it in object
    @get_width.setter
    def set_width(self, width):
        """setter method to change the value 'width' using an object"""
        self.__width = width

    # getter method to get the properties of height
    @property
    def get_height(self):
        """getter method to get the properties of height"""
        return self.__height

    # setting new values for height and updating it in object
    @get_height.setter
    def set_height(self, height):
        """setter method to change the value 'height' using an object"""
        self.__height = height

    # getter method to get the properties of x
    @property
    def get_x(self):
        """getter method to get the properties of x"""
        return self.__x

    # setting new values for x and updating it in object
    @get_x.setter
    def set_x(self, x):
        """setter method to change the value 'x' using an object"""
        self.__x = x

     # getter method to get the properties of y
    @property
    def get_y(self):
        """getter method to get the properties of y"""
        return self.__y

    # setting new values for y and updating it in object
    @get_y.setter
    def set_x(self, y):
        """setter method to change the value 'y' using an object"""
        self.__y = y
