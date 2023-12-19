#!/usr/bin/python3
"""
Module for dividing all elements of a matrix
"""

def matrix_divided(matrix, div):
    """
    Divides elementse of matrix by number

    Args:
    matrix (list): List of lists of integer
    div (int/float): Number to divide by

    Returns:
    list: New divided matrix 

    Raises:
    TypeError: If matrix containg non-numeric elements/div is not a number or is zero
    """
    if not all(isinstance(row, list) for row matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
