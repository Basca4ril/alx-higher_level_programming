#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div2 = []

    for k in my_list:
        mul2 = k % 2 == 0
        div2.append(mul2)

    return div2
