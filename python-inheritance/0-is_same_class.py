#!/usr/bin/python3
"""returning objecT instance """


def is_same_class(obj, a_class):
    """
    returning object exact instance 
    of the specified class 
    """
    if isinstance(obj, a_class):
        return True
    return False
