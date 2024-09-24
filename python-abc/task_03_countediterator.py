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
        self.len = len(some_iterable)

    def __iter__(self):
        """ Returns the iterator object itself.

            Returns:
                self: The iterator object itself.
        """
        return self

    def __next__(self):
        """ Returns the next item from the iterator.

            Raises:
                StopIteration: If there are no more items to iterate.

            Returns:
                object: The next item from the iterator.
        """
        self.count += 1
        if self.count > self.len:
            raise StopIteration

        return next(self.iterator)

    def get_count(self):
        """ returns the current value of the counter """
        return self.count
