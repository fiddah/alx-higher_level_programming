#!/usr/bin/python3
"""Rectangle module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initializing"""
        self.__width = width
        self.__height = height
        """validating width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """A method that returns the rectangle area."""
        return self.__width * self.__height

    def __str__(self):
        """A method that creates a string object from a given object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
