#!/usr/bin/python3
"""base geometry module"""


class BaseGeometry():
    """raises an error if area is not implemented"""
    def area(self):
        raise Exception('area() is not implemented')
