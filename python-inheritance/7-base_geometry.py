#!/usr/bin/python3
""" define a class BaseGeometry """


class BaseGeometry:
    """ a class BaseGeometry """

    def area(self):
        """ raise an Exception with the message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """  validate value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
