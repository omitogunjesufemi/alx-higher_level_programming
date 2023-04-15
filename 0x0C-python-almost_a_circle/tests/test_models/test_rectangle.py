#!/usr/bin/python3
"""This module contains unittest for the Rectangle class
"""
import unittest
from model.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Test Cases for the Rectangle Class
    """

    def setUp(self):
        """This sets up the rectangle class
        """
        self.rectangle_1 = Rectangle(10, 2)
        self.rectangle_2 = Rectangle(2, 10)
        self.rectangle_3 = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self):
        """
        """
        pass

    def test_rectangle_is_created(self):
        """
        """
        self.assertTrue(isinstance(self.rectangle_1, Rectangle))
        self.assertTrue(isinstance(self.rectangle_2, Rectangle))
        self.assertTrue(isinstance(self.rectangle_3, Rectangle))

    def test_rectangle_has_an_id(self):
        """
        """
        pass
