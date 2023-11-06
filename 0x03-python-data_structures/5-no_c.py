#!/usr/bin/python3
def no_c(my_string):
    nstring = ""
    for k in my_string:
        if k != 'c' and k != 'C':
            nstring += k

    return nstring

