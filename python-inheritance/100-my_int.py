#!/usr/bin/python3
"""MyInt"""


class MyInt(int):
    """ MyInt has == and != operators inverted """
    def __eq__(self, other):
        """override the == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """override the != operator"""
        return super().__eq__(other)
