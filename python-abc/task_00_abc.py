#!/usr/bin/env python3
""" Define an abstract class and two subclasses of Animal """
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    """ Define the Animal class """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """ a subclass Dog that inherits from the Animal class """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """ a subclass Cat that inherits from the Animal class """

    def sound(self):
        return "Meow"
