#!/usr/bin/python3
def uniq_add(my_list=[]):
    ints = set()

    for i in my_list:
        if i not in ints:
            ints.add(i)

    tot = sum(ints)

    return tot 
