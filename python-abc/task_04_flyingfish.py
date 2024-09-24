#!/usr/bin/env python3
""" Construct a FlyingFish class that inherits
    from both a Fish class and a Bird class
"""


class Fish:
    """ Defines the Fish class """

    def swim(self):
        """ prints the message of swim of Fish class  """
        print("The fish is swimming")

    def habitat(self):
        """ prints the message of habitat of Fish class """
        print("The fish lives in water")


class Bird:
    """ Defines the Bird class """

    def fly(self):
        """ prints the message of fly of Bird class  """
        print("The bird is flying")

    def habitat(self):
        """ prints the message of habitat of Bird class """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """ Defines the FlyingFish class that inherits from both Fish and Bird """

    def swim(self):
        """ prints the message of swim of FlyingFish class  """
        print("The flying fish is swimming!")

    def fly(self):
        """ prints the message of fly of FlyingFish class  """
        print("The flying fish is soaring!")

    def habitat(self):
        """ prints the message of habitat of FlyingFish class """
        print("The flying fish lives both in water and the sky!")
