#!/usr/bin/python3

""" defining a function that divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """ dividing all elements of a matrix"""

    """ matrix must be a list of lists"""
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(msg)

    """ Div must be a number"""
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    """division by zero error"""
    if div == 0:
        raise ZeroDivisionError('division by zero')

    """All elements of the matrix should be divided by div"""
    new_matrix = []
    for row in matrix:
        if type(row) != list:
            raise TypeError(msg)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        n_matrix = []
        for c in row:
            if type(c) != int and type(c) != float:
                raise TypeError(msg)
            n_matrix.append(round(c/div, 2))
        new_matrix.append(n_matrix)
    return new_matrix
