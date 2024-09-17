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
        """
        self.size = size

    @property
    def size(self):
        """ Get the size of the square

            return:
                the size of squere
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the square

        Args:
            value(int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ method that returns the current square area

        Return:
            square area
        """

        return self.__size ** 2
