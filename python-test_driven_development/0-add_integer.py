#!/usr/bin/python3

"""
This module provides functions to add integers.
Functions:
    add_integers(a, b): Returns the sum of two integers.
"""

def add_integer(a, b=98):

    """
    Returns the sum of two integers.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
