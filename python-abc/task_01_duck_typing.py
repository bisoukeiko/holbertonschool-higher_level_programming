#!/usr/bin/env python3
""" Define an abstract class and two subclasses of Shape """
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """ Define the Shape class """

    @abstractmethod
    def area(self):
        """ Abstract method to calculate the area of the shape. """
        pass

    @abstractmethod
    def perimeter(self):
        """ Abstract method to calculate the perimeter of the shape. """
        pass


class Circle(Shape):
    """ Define the Circle class """

    def __init__(self, radius):
        """ Instantiation radius """
        self.radius = radius

    def area(self):
        """ Return the area of the circle """
        return self.radius ** 2 * math.pi

    def perimeter(self):
        """ Return the perimeter of the circle """
        return self.radius * 2 * math.pi


class Rectangle(Shape):
    """ Define the Rectangle class """

    def __init__(self, width, height):
        """ Instantiation width and height """
        self.width = width
        self.height = height

    def area(self):
        """ Return the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Return the perimeter of the rectangle """
        return (self.width * 2) + (self.height * 2)


def shape_info(obj):
    """ Print the area and perimeter of the shape passed to the function """
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
