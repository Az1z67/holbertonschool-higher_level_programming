#!/usr/bin python3
'''
This mudule create a class named VerboseList
that extends the Python list class. 
'''


class VerboseList(list):
    '''A subclass of list that prints messages on modifications'''

    def append(self, item):
        '''Appends an item to the list and prints a message'''
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        '''Extends the list with items and prints a message'''
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        '''Removes an item from the list and prints a message'''
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=None):
        '''Pops an item from the list and prints a message'''
        if index is None:
            item = super().pop()
        else:
            item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
