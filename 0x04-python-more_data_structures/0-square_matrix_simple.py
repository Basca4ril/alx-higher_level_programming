#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return []
    def squarenum(num):
        return num ** 2

    res = list(map(lambda row: list(map(squarenum, row)), matrix))

    return res
