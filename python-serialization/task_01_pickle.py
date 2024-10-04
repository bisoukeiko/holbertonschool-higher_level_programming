#!/usr/bin/env python3
"""    Python - Serialization - task1
"""
import pickle


class CustomObject:
    """ Define a class that serialize and deserialize custom Python objects """

    def __init__(self, name, age, is_student):
        """ Initialization """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """ Print out the object’s attributes """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """ Serialize the current instance of the object
            and save it to the file
        """
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """ Load and return an instance of the object from the file """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
