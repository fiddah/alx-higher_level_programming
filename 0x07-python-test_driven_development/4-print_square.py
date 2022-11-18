#!/usr/bin/python3
""""A module to print a square with the character # """


def print_square(size):
    """a print square function"""
    if not isinstance(size, int):
        raise TypeError('size must be integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
