#!/usr/bin/python3
""" Class that defines a square """


class Square:
    """ A class used to represent a Square """

    def __init__(self, size=0, position=(0, 0)):
        """ __init__ method

        Args:
            size(int): The size of the square.
            position(tuple): The position of the square.

        Attributes:
            size(int): The size of the square.
            position(tuple): The position of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Get the position of the square

            return:
                the position of the squere
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Set the position of the square

        Args:
            value(tuple): The position of the square.

        Raise:
            TypeError: If the tuple is not 2 positive integers.
        """

        if (type(value) is not tuple
                or len(value) != 2
                or (type(value[0]) is not int or type(value[1]) is not int)
                or (value[0] < 0 or value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ method that returns the current square area

        Return:
            square area
        """

        return self.__size ** 2

    def my_print(self):
        """ method that prints in stdout the square with the character # """

        if self.size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print("\n" * self.__position[1], end="")

            for index in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
