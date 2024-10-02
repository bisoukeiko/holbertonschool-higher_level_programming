#!/usr/bin/python3
""" Define a script that adds all arguments to a Python list,
    and then save them to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
args = sys.argv
new_list = []

for index in range(1, len(args)):
    new_list.append(args[index])

try:
    file_list = load_from_json_file(filename)
except FileNotFoundError:
    file_list = []

file_list.extend(new_list)

save_to_json_file(file_list, filename)
