#!/usr/bin/python3
"""Same class or inherit """


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj inherits from the given `a_class` 
    or if the object is an instance of a class that inherited from
    """
    if isinstance(obj, a_class):
        return True
    return False
