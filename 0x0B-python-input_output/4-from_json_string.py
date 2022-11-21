#!/usr/bin/python3
"""returns from json the representation of an object"""

import json


def from_json_string(my_str):
    """from json the representation to python data structure"""
    return json.loads(my_str)
