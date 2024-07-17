#!/usr/bin/python3
'''
Create a class named CountedIterator that extends
the built-in iterator obtained from the iter function.
'''


class CountedIterator:
    '''A custom iterator that counts items iterated over.'''

    def __init__(self, iterable):
        '''Initialize with an iterable, set up the iterator and counter.'''
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        '''Return the number of items that have been iterated over.'''
        return self.counter

    def __next__(self):
        '''Return the next item and increment the counter.'''
        item = next(self.iterator)
        self.counter += 1
        return item
