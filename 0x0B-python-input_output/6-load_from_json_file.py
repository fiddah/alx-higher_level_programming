#!/usr/bin/python3
"""Json representation from to object"""

import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
