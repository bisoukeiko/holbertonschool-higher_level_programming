#!/usr/bin/env python3
""" Construct a class Dragon that inherits from
    both SwimMixin and FlyMixin
"""


class SwimMixin:
    """ Defines the class SwimMixin. """

    def swim(self):
        """ prints the message of swim of the class SwimMixin. """
        print("The creature swims!")


class FlyMixin:
    """ Defines the class FlyMixin """

    def fly(self):
        """ prints the message of fly of the class FlyMixin. """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """ Defines the class Dragon that inherits
        from both SwimMixin and FlyMixin.
    """

    def roar(self):
        """ prints the message of roar of the class Dragon. """
        print("The dragon roars!")
