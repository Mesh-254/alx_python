#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square value
        of all integers of a matrix 
        args:integers of a matrix. 
    """
    new_matrix = map(lambda x: x*x, matrix)
    return new_matrix
