#!/usr/bin/env python3
""""
    Python - Serialization - task0
"""
import json


def serialize_and_save_to_file(data, filename):
    """  serialize a Python dictionary to a JSON file """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """ deserialize the JSON file to recreate the Python Dictionary """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
