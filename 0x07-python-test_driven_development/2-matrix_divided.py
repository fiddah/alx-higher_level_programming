#!/usr/bin/python3

""" defining a function that divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """ dividing all elements of a matrix"""

    """ matrix must be a list of lists"""
    if type(matrix) is not list or (len(matrix) == 0) or type(matrix[0]) is not list or (len(matrix[0]) == 0):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    """ Div must be a number"""
    if type(div) != int or type(div) != float:
        raise TypeError('div must be a number')

    """division by zero error"""
    if div == 0:
        raise ZeroDivisionError('division by zero')

    """All elements of the matrix should be divided by div, rounded to 2 decimal places"""
    new_matrix = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for c in row:
            if type(c) != int and type(c) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return [[round(i / div, 2) for i in row] for row in matrix]
