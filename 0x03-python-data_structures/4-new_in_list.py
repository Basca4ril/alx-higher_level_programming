#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newls = []
    i = len(my_list)
    if idx < 0 or idx > i:
        return my_list
    newls = list(my_list)
    newls[idx] = element
    return newls
