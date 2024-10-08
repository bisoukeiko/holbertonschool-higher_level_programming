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

    def area(self):
        """ Return the rectangle area """
        return self.__width * self.__height

    def __str__(self):
        """ Return the rectangle description """
        class_name = self.__class__.__name__
        return "[{}] {}/{}".format(class_name, self.__width, self.__height)
