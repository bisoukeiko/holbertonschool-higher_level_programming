#!/usr/bin/env python3
""" Define a class VerboseList that extends the Python list class """


class VerboseList(list):
    """ Define a class VerboseList that inherits from
        the built-in list class
    """

    def append(self, item):
        """ adding the item to the list """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """ extending the list """
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, value):
        """ removing the item from the list """
        if value in self:
            print("Removed [{}] from the list.".format(value))
            super().remove(value)
        else:
            raise ValueError("[{}] not in list".format(value))

    def pop(self, index=-1):
        """ popping the item from the list """
        if not self:
            raise IndexError("list is empty.")
        elif index >= -1 and index < len(self):
            print("Popped [{}] from the list".format(self[index]))
            return super().pop(index)
        else:
            raise IndexError("list index[{}] out of range".format(index))
