#!/usr/bin/python3
""" creating a function that returns a list of available
attributes and methods of an object
"""


def lookup(obj):
    """ a function tha returns a list of object"""
    return dir(obj)
