
#!/usr/bin/python3
'''
Construct a FlyingFish class that inherits from
both a Fish class and a Bird class.'''


class Fish:
    '''Defines a Fish'''

    def swim(self):
        '''swim method'''
        print("The fish is swimming")

    def habitat(self):
        '''habitat method'''
        print("The fish lives in water")


class Bird:
    '''Defines a Bird'''

    def fly(self):
        '''fly method'''
        print("The bird is flying")

    def habitat(self):
        '''habitate method'''
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    '''Defines a FlyingFish'''

    def fly(self):
        '''Override fly method'''
        print("The flying fish is soaring!")

    def swim(self):
        '''Override swim method'''
        print("The flying fish is swimming!")

    def habitat(self):
        '''Override habitat method'''
        print("The flying fish lives both in water and the sky!")

