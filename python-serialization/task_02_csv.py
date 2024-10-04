#!/usr/bin/env python3
"""
    Python - Serialization - task2
"""
import csv
import json

json_filename = "data.json"


def convert_csv_to_json(filename):
    """ Write the JSON data to the file"""
    try:
        with open(filename, "r") as csvf:
            csvReader = csv.DictReader(csvf)
            row = list(csvReader)

        with open(json_filename, "w") as jsonf:
            jsonf.write(json.dumps(row, indent=4))

        return True

    except FileNotFoundError:
        return False
