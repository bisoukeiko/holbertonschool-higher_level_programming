#!/usr/bin/python3
""" define a class MyList """


class MyList(list):
    """ a class that inherits from list """

    def print_sorted(self):
        """ print the list, but sorted (ascending sort) """
        return print(sorted(self))
