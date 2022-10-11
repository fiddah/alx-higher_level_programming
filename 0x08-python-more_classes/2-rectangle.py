#!/usr/bin/python3
"""
This module defines the a Rectangle Object.
"""


class Rectangle:
    """
creating a rectangle with getter and setter method.
"""

    def _init_(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
           raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
           raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
"""calculate the area of a rectanglé"""

         return self.__width * self.__height

    def perimeter(self):
"""calculate th area of  rectanlge"""

        if self.__width == 0 or self.__height == 0
            return 0
        return (self.__width + self.__height) * 2
