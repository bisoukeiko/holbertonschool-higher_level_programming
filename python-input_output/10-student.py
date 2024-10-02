#!/usr/bin/python3
""" Define a class Student that defines a student """


class Student():
    """ a class Student that defines a student """

    def __init__(self, first_name, last_name, age):
        """ Initialize a new student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieve a dictionary representation of a Student instance """
        dict = self.__dict__
        new_dict = {}

        if type(attrs) is list:
            for key in attrs:
                if key in dict:
                    new_dict[key] = dict[key]

            return new_dict
        else:
            return dict
