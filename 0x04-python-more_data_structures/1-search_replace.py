#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list2 = []

    for i in my_list:
        if i == search:
            list2.append(replace)
        else:
            list2.append(i)
    return list2
