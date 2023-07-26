#!/usr/bin/python3
def no_c(my_string):
    """ function that removes all 
    characters c and C from a string.
    """
    new_string = my_string.translate(str.maketrans('','','cC'))
    return new_string

    # Other ways to manipulate strings
        # new_string = re.sub('c|C', "" , my_string)
        # new_string = my_string.strip('Cc')

    