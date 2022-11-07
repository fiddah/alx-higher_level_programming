#!/usr/bin/python3

""" defining a function that divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """ dividing all elements of a matrix"""

    """ matrix must be a list of lists"""
    if matrix is None or len(matrix) == 0:
        raise TypeError(' matrix must be a matrix (list of lists) of integers/floats')

    """Each row of the matrix must have the same size"""
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")

    """ Div must be a number"""
    if type(div) != int or type(div) != float:
        raise TypeError('div must be a number')

    """division by zero error"""
    if div == 0:
        raise ZeroDivisionError('division by zero')

    """All elements of the matrix should be divided by div, rounded to 2 decimal places"""
    new_matrix = []
    div = 0
    for i in matrix:
        new_matrix = matrix[i] / div
        return(round(new_matrix, 2))

