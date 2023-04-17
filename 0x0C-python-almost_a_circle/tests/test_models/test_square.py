#!/usr/bin/python3
"""This module contains unittest for the Square class
"""
import unittest
import sys
import io
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """Test Cases for the Square Class
    """
    def setUp(self):
        """This sets up the Square class
        """
        self.square_1 = Square(5, 0, 0, 1)
        self.square_2 = Square(2, 1, 3, 2)
        self.square_3 = Square(4, 0, 0, 12)

    def tearDown(self):
        """Tears down the setup
        """
        pass

    def test_square_is_created(self):
        """Check if the square was created successfully
        """
        self.assertTrue(isinstance(self.square_1, Square))
        self.assertTrue(isinstance(self.square_2, Square))
        self.assertTrue(isinstance(self.square_3, Square))

    def test_square_has_an_id(self):
        """Check if the created square has an id
        """
        self.assertTrue(self.square_1.id)
        self.assertTrue(self.square_2.id)
        self.assertTrue(self.square_3.id)

    def test_square_width_is_int(self):
        """Check if it is an instance of int
        """
        self.assertTrue(isinstance(self.square_1.width, int))
        self.assertTrue(isinstance(self.square_2.width, int))
        self.assertTrue(isinstance(self.square_3.width, int))

    def test_square_width_is_expected_value(self):
        """Check the expected value of width
        """
        self.assertEqual(self.square_1.width, 5)
        self.assertEqual(self.square_2.width, 2)
        self.assertEqual(self.square_3.width, 4)

    def test_square_height_is_expected_value(self):
        """Check the expected value of height
        """
        self.assertEqual(self.square_1.height, 5)
        self.assertEqual(self.square_2.height, 2)
        self.assertEqual(self.square_3.height, 4)

    def test_square_id_is_expected_value(self):
        """Check the expected value of id
        """
        self.assertEqual(self.square_1.id, 1)
        self.assertEqual(self.square_2.id, 2)
        self.assertEqual(self.square_3.id, 12)

    def test_square_x_is_expected_value(self):
        """Check the expected value of x
        """
        self.assertEqual(self.square_1.x, 0)
        self.assertEqual(self.square_2.x, 1)
        self.assertEqual(self.square_3.x, 0)

    def test_square_y_is_expected_value(self):
        """Check the expected value of x
        """
        self.assertEqual(self.square_1.y, 0)
        self.assertEqual(self.square_2.y, 3)
        self.assertEqual(self.square_3.y, 0)

    def test_square_height_is_int(self):
        """Check if it is an instance of int
        """
        self.assertTrue(isinstance(self.square_1.height, int))
        self.assertTrue(isinstance(self.square_2.height, int))
        self.assertTrue(isinstance(self.square_3.height, int))

    def test_square_width_equal_height(self):
        """Check if width equals height
        """
        self.assertEqual(self.square_1.width, self.square_1.height)
        self.assertEqual(self.square_2.width, self.square_2.height)
        self.assertEqual(self.square_3.width, self.square_3.height)

    def test_square_x_is_int(self):
        """Check if it is an instance of int
        """
        self.assertTrue(isinstance(self.square_1.x, int))
        self.assertTrue(isinstance(self.square_2.x, int))
        self.assertTrue(isinstance(self.square_3.x, int))

    def test_square_y_is_int(self):
        """Check if it is an instance of int
        """
        self.assertTrue(isinstance(self.square_1.y, int))
        self.assertTrue(isinstance(self.square_2.y, int))
        self.assertTrue(isinstance(self.square_3.y, int))

    def test_square_width_is_not_int(self):
        """TypeError is raised when it is not an integer
        """
        with self.assertRaises(TypeError):
            self.square_1.width = "32"
        with self.assertRaises(TypeError):
            self.square_1.width = ["32", 12]
        with self.assertRaises(TypeError):
            self.square_2.width = (12,)
        with self.assertRaises(TypeError):
            self.square_3.width = {}
        with self.assertRaises(TypeError):
            self.square_3.width = 12.0

    def test_square_height_is_not_int(self):
        """TypeError is raised when it is not an integer
        """
        with self.assertRaises(TypeError):
            self.square_1.height = "32"
        with self.assertRaises(TypeError):
            self.square_1.height = ["32", 12]
        with self.assertRaises(TypeError):
            self.square_2.height = (12,)
        with self.assertRaises(TypeError):
            self.square_3.height = {}
        with self.assertRaises(TypeError):
            self.square_3.height = 12.0

    def test_square_x_position_is_not_int(self):
        """TypeError is raised when it is not an integer
        """
        with self.assertRaises(TypeError):
            self.square_1.x = "32"
        with self.assertRaises(TypeError):
            self.square_1.x = ["32", 12]
        with self.assertRaises(TypeError):
            self.square_2.x = (12,)
        with self.assertRaises(TypeError):
            self.square_3.x = {}
        with self.assertRaises(TypeError):
            self.square_3.x = 12.0

    def test_square_y_position_is_not_int(self):
        """TypeError is raised when it is not an integer
        """
        with self.assertRaises(TypeError):
            self.square_1.y = "32"
        with self.assertRaises(TypeError):
            self.square_1.y = ["32", 12]
        with self.assertRaises(TypeError):
            self.square_2.y = (12,)
        with self.assertRaises(TypeError):
            self.square_3.y = {}
        with self.assertRaises(TypeError):
            self.square_3.y = 12.0

    def test_square_width_less_or_equal_zero(self):
        """ValueError is raised when it is <= 0
        """
        with self.assertRaises(ValueError):
            self.square_1.width = 0
        with self.assertRaises(ValueError):
            self.square_2.width = -12
        with self.assertRaises(ValueError):
            self.square_3.width = -32

    def test_square_height_less_or_equal_zero(self):
        """ValueError is raised when it is <= 0
        """
        with self.assertRaises(ValueError):
            self.square_1.height = 0
        with self.assertRaises(ValueError):
            self.square_2.height = -12
        with self.assertRaises(ValueError):
            self.square_3.height = -32

    def test_square_x_less_than_zero(self):
        """ValueError is raised when it is < 0
        """
        with self.assertRaises(ValueError):
            self.square_1.x = -1
        with self.assertRaises(ValueError):
            self.square_2.x = -12
        with self.assertRaises(ValueError):
            self.square_3.x = -34

    def test_square_y_less_than_zero(self):
        """ValueError is raised when it is < 0
        """
        with self.assertRaises(ValueError):
            self.square_1.y = -1
        with self.assertRaises(ValueError):
            self.square_2.y = -12
        with self.assertRaises(ValueError):
            self.square_3.y = -34

    def test_square_string_output(self):
        """Test __str__ method
        """
        expected_output_1 = "[Square] (1) 0/0 - 5"
        expected_output_2 = "[Square] (2) 1/3 - 2"
        expected_output_3 = "[Square] (12) 0/0 - 4"

        self.assertEqual(self.square_1.__str__(), expected_output_1)
        self.assertEqual(self.square_2.__str__(), expected_output_2)
        self.assertEqual(self.square_3.__str__(), expected_output_3)

    def test_square_area(self):
        """Test Square Area
        """
        self.assertEqual(self.square_1.area(), 25)
        self.assertEqual(self.square_2.area(), 4)
        self.assertEqual(self.square_3.area(), 16)

    def test_square_display(self):
        """Test Square Display
        """
        buff_1 = io.StringIO()
        buff_2 = io.StringIO()
        buff_3 = io.StringIO()

        sys.stdout = buff_1
        self.square_1.display()
        output_1 = buff_1.getvalue()

        sys.stdout = buff_2
        self.square_2.display()
        output_2 = buff_2.getvalue()

        sys.stdout = buff_3
        self.square_3.display()
        output_3 = buff_3.getvalue()

        sys.stdout = sys.__stdout__

        expected_output_1 = "#####\n#####\n#####\n#####\n#####\n"
        expected_output_2 =("\n\n\n ##\n ##\n")
        expected_output_3 = ("####\n####\n####\n####\n")

        self.assertEqual(output_1, expected_output_1)
        self.assertEqual(output_2, expected_output_2)
        self.assertEqual(output_3, expected_output_3)
