#!/usr/bin/python3
"""Square module: returns the area of a square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""
    def __init__(self, size):
        """initializing"""
        self.__size = size
        """validating size"""
        self.integer_validator("size", size)

    def area(self):
        """A method that returns the area of a square."""
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size) 
