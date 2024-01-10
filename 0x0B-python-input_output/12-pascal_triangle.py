#!/usr/bin/python3
"""Module for a Pascal's Triangle function."""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the given number of rows.

    Args:
        n (int): Number of rows in Pascal's Triangle.

    Returns:
        list: List of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    # Initialize Pascal's Triangle with the first row
    triangle = [[1]]

    # Generate the remaining rows
    for i in range(1, n):
        row = [1]  # The first element of each row is always 1
        for j in range(1, i):
            # Calculate the value using the elements from the previous row
            value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(value)
        row.append(1)  # The last element of each row is always 1
        triangle.append(row)

    return triangle
