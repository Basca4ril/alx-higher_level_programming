#!/usr/bin/python3
def print_matrix_integer(martix=[[]]):
    if not matrix:
        print()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j != len(matrix[i]) - 1:
                ends = ' '
            else:
                ends = ''
            print("{:d}".format(matrix[i][j]), end=ends)
        print()
