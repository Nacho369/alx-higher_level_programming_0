#!/usr/bin/python3

"""Define the add_item() function"""

import sys
save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file


def add_item(args, filename):
    try:
        list_args = load_from_json(filename)
    except:
        list_args = []

    for item in args:
        list_args.append(item)

    save_to_json(list_args, filename)

if __name__ == "__main__":
    args = sys.argv[1:]
    filename = "add_item.json"
    add_item(args, filename)
