#!/usr/bin/python3

"""  function that prints a square with the character # """


def print_square(size):
    """
        Args:
            size(integer): the size length of the square
        Raises:
            TypeError: If the size is not a integer.
            ValueError: If the size is less than 0.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for index in range(size):
        print("#" * index)
