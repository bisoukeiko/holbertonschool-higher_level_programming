#!/usr/bin/env python3
""" Define an abstract class and two subclasses of Shape """
from abc import ABCMeta, abstractmethod
import math


class Shape(metaclass=ABCMeta):
    """ Define the Shape class """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """ Define the Circle class """

    def __init__(self, radius):
        """ Instantiation radius """
        self.__radius = radius

    def area(self):
        """ Return the area of the circle """
        return self.__radius ** 2 * math.pi

    def perimeter(self):
        """ Return the perimeter of the circle """
        return abs(self.__radius) * 2 * math.pi


class Rectangle(Shape):
    """ Define the Rectangle class """

    def __init__(self, width, height):
        """ Instantiation width and height """
        self.__width = width
        self.__height = height

    def area(self):
        """ Return the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Return the perimeter of the rectangle """
        return (self.__width * 2) + (self.__height * 2)


def shape_info(obj):
    """ Print the area and perimeter of the shape passed to the function """
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
