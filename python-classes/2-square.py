#!/usr/bin/python3
""" Class that defines a square """


class Square:
    """ A class used to represent a Square """

    def __init__(self, size=0):
        """ __init__ method

        Args:
            size(int): The size of the square.

        Attributes:
            __size(int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
