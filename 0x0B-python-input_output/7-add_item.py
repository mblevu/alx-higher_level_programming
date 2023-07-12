#!/usr/bin/python3
import sys
from os.path import exists

"""adds all arguments to a python list"""
if __name__ == "__main__":
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    items = load(filename)
except FileNotFoundError:
    items = []
items.extend(sys.argv[1:])
save(items, filename)
