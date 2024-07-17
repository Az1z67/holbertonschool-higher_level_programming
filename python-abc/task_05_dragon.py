#!/usr/bin/python3
'''
Design two mixin classes, SwimMixin and FlyMixin
'''


class SwimMixin:
    '''Mixin class for swimming'''

    def swim(self):
        '''swim method'''
        print("The creature swims!")


class FlyMixin:
    '''Mixin class for flying'''

    def fly(self):
        '''fly method'''
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    '''Class representing a dragon'''

    def roar(self):
        '''roar function'''
        print("The dragon roars!")
