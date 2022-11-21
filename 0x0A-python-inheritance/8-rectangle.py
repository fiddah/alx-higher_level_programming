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
