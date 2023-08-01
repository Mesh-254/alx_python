#!/usr/bin/python3
""" Returns True if the object is an instance
    of a class that inherited
    (directly or indirectly)
"""


def inherits_from(obj, a_class):
    """ returns True if object is an instance
      of a class that is inherited
      directly or indirectly
    """
    # loops through subclasses in class
    for cls in a_class.__subclasses__():
        if isinstance(obj, cls):
            return True
    return False
