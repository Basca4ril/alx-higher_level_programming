#!/usr/bin/python3
def common_elements(set_1, set_2):
    comm = set()
    for i in set_1:
        for k in set_2:
            if i == k:
                comm.add(i)
    return comm
