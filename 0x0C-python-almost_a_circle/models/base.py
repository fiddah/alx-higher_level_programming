#!/usr/bin/python3
"""Base module"""

import json


class Base():
    """creating a class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializing base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
