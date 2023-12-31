#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
        prints a matrix of integers.
        Args:
            matrix: A list of lists,
            where each inner list represents
            a row in the matrix.
    """
    for row in matrix:
        print(" ".join("{:d}".format(column) for column in row))
