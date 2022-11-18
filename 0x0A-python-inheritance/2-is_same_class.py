#!/usr/bin/python3
"""func that return true
   if an object is exactly an 
   instance of the specified class 
"""


def is_same_class(obj, a_class):
    """is an instance of class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
