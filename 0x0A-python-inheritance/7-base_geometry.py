#!/usr/bin/python3
"""base geometry module"""


class BaseGeometry():
    """BaseGeometry Class"""
    def area(self):
        """raises an error if area is not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError('{:s} must be integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
