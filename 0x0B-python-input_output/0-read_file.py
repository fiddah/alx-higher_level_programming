#!/usr/bin/python3
"""Ä module that reads a text file"""


def read_file(filename=""):
    """a func that reads a texts file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
