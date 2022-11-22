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

    @property
    def height(self):
        """return a private attribute"""
        return self.__height

    @property
    def x(self):
        """return a private attribute"""
        return self.__x

    @property
    def y(self):
        """return a private attribute"""
        return self.__y
