#!/usr/bin/python3
"""A func that prints first name and last name"""


def say_my_name(first_name, last_name=""):
    """ first name and last name must be a string """
    if first_name != str:
        raise TypeError('first_name must be a string')
    if last_name != str:
        raise TypeError('last_name must be a string')
    print('My name is {} {}' .format(first_name, last_name))
