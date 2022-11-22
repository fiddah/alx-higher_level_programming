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
    def width(self, value):
        """setting the private attribute"""
        self.__width = value

    @property
    def height(self):
        """return a private attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the private attribute"""
        self.__height = value

    @property
    def x(self):
        """return a private attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting the private attribute"""
        self.__x = value

    @property
    def y(self):
        """return a private attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting the private attribute"""
        self.__y = value
