#!/usr/bin/python3
"""Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """Creating a rectangle class that inherits from the base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """return a private attribute"""
        return self.__width

    @width.setter
    def width(self, width, value):
        """setting the private attribute"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('{} must be > 0'.format(width))
        self.__width = value

    @property
    def height(self):
        """return a private attribute"""
        return self.__height

    @height.setter
    def height(self, height, value):
        """setting the private attribute"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(height))
        if value <= 0:
            raise ValueError('{} must be > 0'.format(height))
        self.__height = value

    @property
    def x(self):
        """return a private attribute"""
        return self.__x

    @x.setter
    def x(self, x, value):
        """setting the private attribute"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(x))
        if value < 0:
            raise ValueError('{} must be >= 0'.format(x))
        self.__x = value

    @property
    def y(self):
        """return a private attribute"""
        return self.__y

    @y.setter
    def y(self, y, value):
        """setting the private attribute"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(y))
        if value < 0:
            raise ValueError('{} must be >= 0'.format(y))
        self.__y = value
