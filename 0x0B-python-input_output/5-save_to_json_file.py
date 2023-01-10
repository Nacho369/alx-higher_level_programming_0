#!/usr/bin/python3

"""Define the save_to_json_file() function"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as file_w:
        json.dump(my_obj, file_w)
