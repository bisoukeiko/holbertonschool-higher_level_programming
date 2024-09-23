#!/usr/bin/python3
""" a class Rectangle that inherits from BaseGeometry (7-base_geometry.py) """
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ a class Rectangle that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Instantiation width and height """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
