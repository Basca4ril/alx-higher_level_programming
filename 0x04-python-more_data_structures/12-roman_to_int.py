#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    t = 0
    pv = 0

    for i in roman_string[::-1]:
        num = roman.get(i)
        if num is None:
            return 0
        if num < pv:
            t -= num
        else:
            t += num

        pv = num

    return t
