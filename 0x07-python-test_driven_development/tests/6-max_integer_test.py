#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    """TestMaxInteger is a test class
    """
    def test_max_integer(self):
        """Returns the largest integer in a list"""
        self.assertEqual(max_integer([100, 23, 63, 14]), 100)
        self.assertEqual(max_integer([1, 3, 3, 4]), 4)

    def test_returns_none(self):
        """Returns None for empty list"""
        self.assertEqual(max_integer([]), None)

    def test_non_list_type(self):
        """Return type error for non-list parameters"""
        with self.assertRaises(TypeError):
            max_integer(9)
            max_integer("1234")
            max_integer({"1":2, "3": 1})
            max_integer({3, 5, 6})

    def test_none_parameter(self):
        """Returns None for none parameter"""
        with self.assertRaises(TypeError):
            max_integer(None)
