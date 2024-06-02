#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """ifobject is an instance of a classinherited (directly or indirectly)"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
