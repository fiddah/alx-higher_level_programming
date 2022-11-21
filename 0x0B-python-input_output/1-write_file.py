#!/usr/bin/python3
"""Ä module that writes a string to a text file"""


def write_file(filename="", text=""):
    """write a string to a texts file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
