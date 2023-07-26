#!/usr/bin/python3
def no_c(my_string):
    """ function that removes all 
    characters c and C from a string.
    """
    # Other ways to manipulate strings
    # new_string = my_string.translate(str.maketrans('','','cC'))
    # new_string = re.sub('c|C', "" , my_string)
    new_string = my_string.strip('Cc')

    return new_string
