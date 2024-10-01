#!/usr/bin/python3
""" Define a function that returns an object (Python data structure)
    represented by a JSON string
"""
import json


def from_json_string(my_str):
    return json.loads(my_str)
