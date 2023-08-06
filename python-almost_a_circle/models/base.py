#!/usr/bin/python3
"""Base class module"""


from sys import argv


class Base:
    """base class for our module"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization of the object's state"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
