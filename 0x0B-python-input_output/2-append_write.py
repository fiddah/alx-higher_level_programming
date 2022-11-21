#!/usr/bin/python3
"""Ä module that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends a string at the end of a texts file"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
