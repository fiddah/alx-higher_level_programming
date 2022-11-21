#!/usr/bin/python3
"""A module that returns the 
json the representation of an object"""

import json


def to_json_string(my_obj):
    """returns the json the representation of an object"""
    return json.dumps(my_obj)
