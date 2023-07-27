#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square value
        of all integers of a matrix 
        args:integers of a matrix. 
    """
    new_matrix = list(map(lambda x: list(map(lambda y: y**2, x)), matrix))
    return new_matrix
