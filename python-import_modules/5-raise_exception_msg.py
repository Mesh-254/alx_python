#!/usr/bin/python3
def raise_exception_msg(message=""):
    """Raise an exception with a custom message."""
    try:
        raise NameError(message)
    except NameError:
        raise
