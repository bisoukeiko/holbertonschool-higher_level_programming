#!/usr/bin/python3
""" Define a class Student that defines a student """


class Student():
    """ a class Student that defines a student """

    def __init__(self, first_name, last_name, age):
        """ Initialize a new student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieve a dictionary representation of a Student instance """

        return self.__dict__
