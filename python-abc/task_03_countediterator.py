#!/usr/bin/env python3
""" a class CountedIterator that extends the built-in iterator obtained
    from the iter function
"""


class CountedIterator:
    """ Define a class CountedIterator """

    def __init__(self, some_iterable):
        """ Instantiation """
        self.count = 0
        self.iterator = iter(some_iterable)

    def get_count(self):
        """ returns the current value of the counter """
        return self.count

    def __next__(self):
        """ Returns the next item from the iterator.

            Raises:
                StopIteration: If there are no items left to iterate.

            Returns:
                object: The next item from the iterator.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """ Returns the iterator object itself.

            Returns:
                self: The iterator object itself.
        """
        return self
