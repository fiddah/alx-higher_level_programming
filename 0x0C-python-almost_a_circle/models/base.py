#!/usr/bin/python3
"""Base module"""


class Base():
    """creating a class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializing base class"""
        if id is None:
            Base.__nb_objects = +1
            self.id = self.__nb_objects
        else:
            __nb_objects = +1
            self.id = self.__nb_objects
