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
    def width(self, value):
        """setter method to change the value 'width' using an object"""
        # validating if width is > than 0 and if it is int type
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # getter method to get the properties of height
    @property
    def height(self):
        """getter method to get the properties of height"""
        return self.__height

    # setting new values for height and updating it in object
    @height.setter
    def height(self, value):
        """setter method to change the value 'height' using an object"""
        # validating if height is > than 0 and if it is int type
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # getter method to get the properties of x
    @property
    def x(self):
        """getter method to get the properties of x"""
        return self.__x

    # setting new values for x and updating it in object
    @x.setter
    def x(self, value):
        """setter method to change the value 'x' using an object"""
        # validating if x is >= 0 and if it is int type
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # getter method to get the properties of y
    @property
    def y(self):
        """getter method to get the properties of y"""
        return self.__y

    # setting new values for y and updating it in object
    @y.setter
    def y(self, value):
        """setter method to change the value 'y' using an object"""
        # validating if y is >= 0 and if it is int type
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method that calculates the area of a rectangle"""
        result_area = (self.__width * self.__height)
        return result_area

    # def display(self):
    #     """prints in stdout the Rectangle instance with the character #"""
    #     for h in range(self.__y):
    #         for w in range(self.__x):
    #             print("", end="")
    #         print()
    #     for h in range(self.__height):
    #         for w in range(self.__width):
    #             print("  ".join("#"), end="")
    #         print()

    def display(self):
        """
           Display The Rectangle Using  '#'
        """
        print(("\n" * self.__y) + "\n".
              join(((" " * self.__x) + ("#" * self.__width))
                   for i in range(self.__height)))

    def __str__(self) -> str:
        """Function returns string representation"""
        return ("[Rectangle] ({:0d}) {:0d}/{:0d} - {:0d}/{:0d}"
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height))
