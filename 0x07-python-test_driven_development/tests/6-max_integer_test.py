#!/usr/bin/python3
"""
Unittests for max_integer function.
"""

import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            max_integer([])

    def test_float_numbers(self):
        with self.assertRaises(TypeError):
            max_integer([1.5, 2.7, 3.0])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3, 4])

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_duplicate_max_value(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 4, 4]), 4)

    def test_large_list(self):
        self.assertEqual(max_integer(list(range(1000000))), 999999)


if __name__ == '__main__':
    unittest.main()

