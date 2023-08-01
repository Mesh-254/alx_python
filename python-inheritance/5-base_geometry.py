#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry:
    """This is the base class for all geometries."""

    def area(self):
        """public instance method that raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if type(value) != int:
            raise TypeError("{:} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:} must be greater than 0".format(name))
