#!/usr/bin/python3
""" Define the function that reads a text file and prints it """


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout """
    with open(filename, encoding="utf-8") as file:
        read_data = file.read()
        print(read_data, end="")
