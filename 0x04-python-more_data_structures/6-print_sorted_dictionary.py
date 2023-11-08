#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary.keys())

    for i in keys:
        val = a_dictionary[i]
        print("{}: {}".format(i, val))
