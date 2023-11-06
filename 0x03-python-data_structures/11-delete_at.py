#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    list2 = []
    for k in range(len(my_list)):
        if k != idx:
            list2.append(my_list[k])

    return list2
