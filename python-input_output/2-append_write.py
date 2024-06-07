#!/usr/bin/python3
"""Append to the file"""


def append_write(filename="", text=""):
"""appends a string to a text file"""
    with open(filename, "a") as f:
        return f.write(text)
