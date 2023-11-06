#!/usr/bin/python3
def print_matrix_integer(martix=[[]]):
    l = len(matrix)
    if not matrix:
        print()
    for i in range(l):
        for k in range(l):
            if i < l and k < len(matrix[i]):
                print("{:d}".format(matrix[i][k]), end=" ")
            else:
                print("0", end=" ")
        print()
