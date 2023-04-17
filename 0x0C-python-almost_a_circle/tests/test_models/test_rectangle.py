#!/usr/bin/python3
"""This module contains unittest for the Rectangle class
"""
import unittest
import io
import sys
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Test Cases for the Rectangle Class
    """

    def setUp(self):
        """This sets up the rectangle class
        """
        self.rectangle_1 = Rectangle(10, 2)
        self.rectangle_2 = Rectangle(2, 20, 1, 3)
        self.rectangle_3 = Rectangle(10, 5, 0, 0, 12)

    def tearDown(self):
        """Tears down the setup
        """
        pass

    def test_rectangle_is_created(self):
        """Check if the rectangle was created successfully
        """
        self.assertTrue(isinstance(self.rectangle_1, Rectangle))
        self.assertTrue(isinstance(self.rectangle_2, Rectangle))
        self.assertTrue(isinstance(self.rectangle_3, Rectangle))

    def test_rectangle_has_an_id(self):
        """Check if the created rectangle has an id
        """
        self.assertTrue(self.rectangle_1.id)
        self.assertTrue(self.rectangle_2.id)
        self.assertTrue(self.rectangle_3.id)

    def test_rectangle_width_is_int(self):
        """Check if it is an instance of int
        """
        self.assertTrue(isinstance(self.rectangle_1.width, int))
        self.assertTrue(isinstance(self.rectangle_2.width, int))
        self.assertTrue(isinstance(self.rectangle_3.width, int))

    def test_rectangle_height_is_int(self):
        """Check if it is an instance of int
        """
        self.assertTrue(isinstance(self.rectangle_1.height, int))
        self.assertTrue(isinstance(self.rectangle_2.height, int))
        self.assertTrue(isinstance(self.rectangle_3.height, int))

    def test_rectangle_x_is_int(self):
        """Check if it is an instance of int
        """
        self.assertTrue(isinstance(self.rectangle_1.x, int))
        self.assertTrue(isinstance(self.rectangle_2.x, int))
        self.assertTrue(isinstance(self.rectangle_3.x, int))

    def test_rectangle_y_is_int(self):
        """Check if it is an instance of int
        """
        self.assertTrue(isinstance(self.rectangle_1.y, int))
        self.assertTrue(isinstance(self.rectangle_2.y, int))
        self.assertTrue(isinstance(self.rectangle_3.y, int))

    def test_rectangle_width_is_not_int(self):
        """TypeError is raised when it is not an integer
        """
        with self.assertRaises(TypeError):
            self.rectangle_1.width = "32"
            self.rectangle_1.width = ["32", 12]
            self.rectangle_2.width = (12)
            self.rectangle_2.width = {width: 12}
            self.rectangle_3.width = {}
            self.rectangle_3.width = 12.0

    def test_rectangle_height_is_not_int(self):
        """TypeError is raised when it is not an integer
        """
        with self.assertRaises(TypeError):
            self.rectangle_1.height = "32"
        with self.assertRaises(TypeError):
            self.rectangle_1.height = ["32", 12]
        with self.assertRaises(TypeError):
            self.rectangle_2.height = (12)

            
            self.rectangle_2.height = {width: 12}
            self.rectangle_3.height = {}
            self.rectangle_3.height = 12.0

    def test_rectangle_x_position_is_not_int(self):
        """TypeError is raised when it is not an integer
        """
        with self.assertRaises(TypeError):
            self.rectangle_1.x = "32"
        with self.assertRaises(TypeError):
            self.rectangle_1.x = ["32", 12]
        with self.assertRaises(TypeError):
            self.rectangle_2.x = (12)
        with self.assertRaises(TypeError):
            self.rectangle_2.x = {width: 12}
        with self.assertRaises(TypeError):
            self.rectangle_3.x = {}
        with self.assertRaises(TypeError):
            self.rectangle_3.x = 12.0

    def test_rectangle_y_position_is_not_int(self):
        """TypeError is raised when it is not an integer
        """
        with self.assertRaises(TypeError):
            self.rectangle_1.y = "32"
            self.rectangle_1.y = ["32", 12]
            self.rectangle_2.y = (12)
            self.rectangle_2.y = {width: 12}
            self.rectangle_3.y = {}
            self.rectangle_3.y = 12.0

    def test_rectangle_width_less_or_equal_zero(self):
        """ValueError is raised when it is <= 0
        """
        with self.assertRaises(ValueError):
            self.rectangle_1.width = 0
        with self.assertRaises(ValueError):
            self.rectangle_2.width = -12
        with self.assertRaises(ValueError):
            self.rectangle_3.width = -32

    def test_rectangle_height_less_or_equal_zero(self):
        """ValueError is raised when it is <= 0
        """
        with self.assertRaises(ValueError):
            self.rectangle_1.height = 0
        with self.assertRaises(ValueError):
            self.rectangle_2.height = -12
        with self.assertRaises(ValueError):
            self.rectangle_3.height = -32

    def test_rectangle_x_less_than_zero(self):
        """ValueError is raised when it is < 0
        """
        with self.assertRaises(ValueError):
            self.rectangle_1.x = -1
        with self.assertRaises(ValueError):
            self.rectangle_2.x = -12
        with self.assertRaises(ValueError):
            self.rectangle_3.x = -34

    def test_rectangle_y_less_than_zero(self):
        """ValueError is raised when it is < 0
        """
        with self.assertRaises(ValueError):
            self.rectangle_1.y = -1
        with self.assertRaises(ValueError):
            self.rectangle_2.y = -12
        with self.assertRaises(ValueError):
            self.rectangle_3.y = -34

    def test_rectangle_area(self):
        """Test Rectangle Area
        """
        self.assertEqual(self.rectangle_1.area(), 20)
        self.assertEqual(self.rectangle_2.area(), 40)
        self.assertEqual(self.rectangle_3.area(), 50)

    def test_rectangle_display(self):
        """Test Rectangle Display
        """
        buff_1 = io.StringIO()
        buff_2 = io.StringIO()
        buff_3 = io.StringIO()

        sys.stdout = buff_1
        self.rectangle_1.display()
        output_1 = buff_1.getvalue()

        sys.stdout = buff_2
        self.rectangle_2.display()
        output_2 = buff_2.getvalue()

        sys.stdout = buff_3
        self.rectangle_3.display()
        output_3 = buff_3.getvalue()

        sys.stdout = sys.__stdout__

        expected_output_1 = "##########\n##########\n"
        expected_output_2 =("\n\n\n ##\n ##\n ##\n ##\n"
                            " ##\n ##\n ##\n ##\n"
                            " ##\n ##\n ##\n ##\n ##\n ##\n ##\n"
                            " ##\n ##\n ##\n ##\n ##\n")
        expected_output_3 = ("##########\n##########\n"
                             "##########\n##########\n##########\n")

        self.assertEqual(output_1, expected_output_1)
        self.assertEqual(output_2, expected_output_2)
        self.assertEqual(output_3, expected_output_3)

    def test_rectangle_string_output(self):
        """Test __str__ method
        """
        expected_output_1 = "[Rectangle] (15) 0/0 - 10/2"
        expected_output_2 = "[Rectangle] (16) 1/3 - 2/20"
        expected_output_3 = "[Rectangle] (12) 0/0 - 10/5"

        self.assertEqual(self.rectangle_1.__str__(), expected_output_1)
        self.assertEqual(self.rectangle_2.__str__(), expected_output_2)
        self.assertEqual(self.rectangle_3.__str__(), expected_output_3)

    def test_rectangle_update_method(self):
        """Test update method works properly
        """
        self.rectangle_1.update(89)
        self.rectangle_1.update(89, 2, 3)
        self.rectangle_1.update(89, 2, 3, 4)
        self.rectangle_1.update(89, 2, 3, 4, 5)
        self.assertEqual(self.rectangle_1.id, 89)
        self.assertEqual(self.rectangle_1.width, 2)
        self.assertEqual(self.rectangle_1.height, 3)
        self.assertEqual(self.rectangle_1.x, 4)
        self.assertEqual(self.rectangle_1.y, 5)

    def test_rectangle_update_raise_exception(self):
        """Raise TypeError Exception
        """
        with self.assertRaises(TypeError):
