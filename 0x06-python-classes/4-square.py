#!/usr/bin/python3

"""Define a class square."""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """An init method for class Square.

        Args:
            size (int): An integer varibale.
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.size = size
    @property
    def size(self):
        """A getter(accessor) method for private instance attribute: size.
        Returns:
            The return value is the private attribute size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """A setter(mutator) method for private instance attribute: size.
        Args:
            value (int): The size of the square.
        """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        """A public instance menthod
        Returns:
            The return value is the area of a square
        """
        return self.__size**2
