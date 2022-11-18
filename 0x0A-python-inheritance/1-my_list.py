#!/usr/bin/python3
"""A module that sorts list"""


class MyList(list):
    """Mylist inherits from list"""
    def __init__(self):
        """initializing the object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted lists"""
        print(sorted(self))
