#!/usr/bin/python3
""" My list"""


class MyList(list):
    """Define my list sorting ascending """
    def print_sorted(self):
        """Function for sorting list"""
        print(sorted(self))
