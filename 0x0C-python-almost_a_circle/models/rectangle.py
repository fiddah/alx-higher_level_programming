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
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """return a private attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the private attribute"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """return a private attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting the private attribute"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """return a private attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting the private attribute"""
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """calculates the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Printing the rectangle in stdout"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """A method that creates a string object from a given object"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,\
                self.__x, self.__y, self.__width, self.__height)
