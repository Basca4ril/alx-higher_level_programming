#!/usr/bin/python3
"""
Module for lazy_matrix_mul function.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        numpy.ndarray: The result of the matrix multiplication.

    Raises:
        ValueError: If m_a or m_b can't be multiplied.
    """
    result = np.dot(m_a, m_b)
    return result

