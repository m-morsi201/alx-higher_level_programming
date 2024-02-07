#!/usr/bin/python3
"""
Module That adds all arguments to a Python list
and then save them to a file
"""

from sys import argv


loadFile = __import__('6-load_from_json_file').load_from_json_file
saveFile = __import__('5-save_to_json_file').save_to_json_file

try:
    jsonList = loadFile('add_item.json')
except (ValueError, FileNotFoundError):
    jsonList = []

for i in argv[1:]:
    jsonList.append(i)

saveFile(jsonList, 'add_item.json')
