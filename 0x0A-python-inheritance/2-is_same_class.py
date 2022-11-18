#!/usr/bin/python3
"""func that return true for instance of the specified class"""


def is_same_class(obj, a_class):
    """is an instance of class"""
    if type(obj) == a_class:
        return True
    else:
        return False
