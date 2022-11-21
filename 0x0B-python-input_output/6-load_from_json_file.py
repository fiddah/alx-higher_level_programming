#!/usr/bin/python3
"""Json representation from to object"""

import json


def load_from_json_file(my_obj, filename):
    """creates an Object from a “JSON file”"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return json.load(f)
