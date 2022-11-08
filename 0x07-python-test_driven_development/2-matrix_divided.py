#!/usr/bin/python3

""" defining a function that divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """ dividing all elements of a matrix"""

    """ matrix must be a list of lists"""
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(msg)

    """ Div must be a number"""
    if type(div) != int or type(div) != float:
        raise TypeError('div must be a number')

    """division by zero error"""
    if div == 0:
        raise ZeroDivisionError('division by zero')

    """All elements of the matrix should be divided by div, 
    rounded to 2 decimal places"""
    new_matrix = []
    for row in matrix:
        if type(row) != list:
            raise TypeError(msg)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for c in row:
            if type(c) != int and type(c) != float:
                raise TypeError(msg)
        new_matrix.append(round(c/div, 2))
    return new_matrix
