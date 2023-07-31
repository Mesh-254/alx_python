#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """returns a list with all values multiplied by a number
    No use of any loops
    """
    new_values = map((lambda x: x*number), my_list)
    newlist = list(new_values)
    return newlist
