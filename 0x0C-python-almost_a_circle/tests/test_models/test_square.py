#!/usr/bin/python3
"""This module contains unittest for the Square class
"""
import unittest
import sys
import io
import os
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
        self.square_4 = Square(1)
        self.square_5 = Square(1, 2)
        self.square_6 = Square(1, 2, 3)

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
        with self.assertRaises(TypeError):
            Square("1")

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
        with self.assertRaises(TypeError):
            Square("1")

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
        with self.assertRaises(TypeError):
            Square(1, "2")

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
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_width_less_or_equal_zero(self):
        """ValueError is raised when it is <= 0
        """
        with self.assertRaises(ValueError):
            self.square_1.width = 0
        with self.assertRaises(ValueError):
            self.square_2.width = -12
        with self.assertRaises(ValueError):
            self.square_3.width = -32
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_height_less_or_equal_zero(self):
        """ValueError is raised when it is <= 0
        """
        with self.assertRaises(ValueError):
            self.square_1.height = 0
        with self.assertRaises(ValueError):
            self.square_2.height = -12
        with self.assertRaises(ValueError):
            self.square_3.height = -32
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_x_less_than_zero(self):
        """ValueError is raised when it is < 0
        """
        with self.assertRaises(ValueError):
            self.square_1.x = -1
        with self.assertRaises(ValueError):
            self.square_2.x = -12
        with self.assertRaises(ValueError):
            self.square_3.x = -34
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_square_y_less_than_zero(self):
        """ValueError is raised when it is < 0
        """
        with self.assertRaises(ValueError):
            self.square_1.y = -1
        with self.assertRaises(ValueError):
            self.square_2.y = -12
        with self.assertRaises(ValueError):
            self.square_3.y = -34
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

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
        expected_output_2 = ("\n\n\n ##\n ##\n")
        expected_output_3 = ("####\n####\n####\n####\n")

        self.assertEqual(output_1, expected_output_1)
        self.assertEqual(output_2, expected_output_2)
        self.assertEqual(output_3, expected_output_3)

    def test_square_size_is_int(self):
        """Check if size is an instance of int
        """
        self.assertTrue(isinstance(self.square_1.size, int))
        self.assertTrue(isinstance(self.square_2.size, int))
        self.assertTrue(isinstance(self.square_3.size, int))

    def test_square_width_is_expected_value(self):
        """Check size is the expected value of width
        """
        self.assertEqual(self.square_1.size, 5)
        self.assertEqual(self.square_2.size, 2)
        self.assertEqual(self.square_3.size, 4)

    def test_square_size_is_not_int(self):
        """TypeError is raised when size is not an integer
        """
        with self.assertRaises(TypeError):
            self.square_1.size = "32"
        with self.assertRaises(TypeError):
            self.square_1.size = ["32", 12]
        with self.assertRaises(TypeError):
            self.square_2.size = (12,)
        with self.assertRaises(TypeError):
            self.square_3.size = {}
        with self.assertRaises(TypeError):
            self.square_3.size = 12.0

    def test_square_size_less_or_equal_zero(self):
        """ValueError is raised when it is <= 0
        """
        with self.assertRaises(ValueError):
            self.square_1.size = 0
        with self.assertRaises(ValueError):
            self.square_2.size = -12
        with self.assertRaises(ValueError):
            self.square_3.size = -32

    def test_square_update_method(self):
        """Test Square update method works properly
        """
        self.square_1.update(10)
        self.square_1.update(10, 2)
        self.square_1.update(10, 2, 3)
        self.square_1.update(10, 2, 3, 4)
        self.assertEqual(self.square_1.id, 10)
        self.assertEqual(self.square_1.size, 2)
        self.assertEqual(self.square_1.x, 3)
        self.assertEqual(self.square_1.y, 4)

    def test_square_update_args_not_empty(self):
        """Test Square update method with a non-empty args
        """
        args = (90, 2, 3, 4)
        self.square_2.update(*args, size=1, y=1, id=100)
        self.assertEqual(self.square_2.id, 90)
        self.assertEqual(self.square_2.size, 2)
        self.assertEqual(self.square_2.x, 3)
        self.assertEqual(self.square_2.y, 4)

    def test_square_update_args_empty(self):
        """Test Square update method with a empty args
        """
        args = ()
        self.square_3.update(*args, sizze=4, id=7)
        self.assertEqual(self.square_3.size, 4)
        self.assertEqual(self.square_3.id, 7)

    def test_square_update_more_than_expected_args(self):
        """
        """
        args = (90, 2, 3, 4, 5, 7)
        self.square_2.update(*args, size=1, x=1, id=100)
        self.assertEqual(self.square_2.id, 90)
        self.assertEqual(self.square_2.size, 2)
        self.assertEqual(self.square_2.x, 3)
        self.assertEqual(self.square_2.y, 4)

    def test_square_update_wrong_kwargs(self):
        """Test update method with attr not in object
        """
        args = ()
        self.square_3.update(x=4, height=7, value=10)
        self.assertEqual(self.square_3.x, 4)
        self.assertEqual(self.square_3.id, 12)

    def test_square_to_dictionary_method_returns_dictionary(self):
        """Test if to_dictionary() returns a dictionary
        """
        self.assertTrue(type(self.square_1.to_dictionary()) is dict)
        self.assertTrue(type(self.square_2.to_dictionary()) is dict)
        self.assertTrue(type(self.square_3.to_dictionary()) is dict)

    def test_square_to_dictionary_method_give_expected_output(self):
        """Test if to_dictionary() method gives the expected
        dictionary values
        """
        output_1 = {'id': 1, 'size': 5, 'x': 0, 'y': 0}
        output_2 = {'id': 2, 'size': 2, 'x': 1, 'y': 3}
        output_3 = {'id': 12, 'size': 4, 'x': 0, 'y': 0}

        self.assertEqual(self.square_1.to_dictionary(), output_1)
        self.assertEqual(self.square_2.to_dictionary(), output_2)
        self.assertEqual(self.square_3.to_dictionary(), output_3)

    def test_square_save_empty_list_for_None_parameter(self):
        """Check it saves an empty file for No parameter
        """
        Square.save_to_file(None)

        with open("Square.json", "r") as json_file:
            output = json_file.read()

        self.assertEqual("[]", output.strip("\n"))

    def test_square_save_empty_list_for_empty_list_param(self):
        """Check it saves an empty file for an empty parameter
        """
        Square.save_to_file([])

        with open("Square.json", "r") as json_file:
            output = json_file.read()

        self.assertEqual("[]", output.strip("\n"))

    def test_square_save_to_file_with_appropriate_params(self):
        """Check it saves an empty file for an empty parameter
        """
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4, 0, 9)
        Square.save_to_file([r1, r2])

        with open("Square.json", "r") as json_file:
            output = json_file.read()

        self.assertEqual("[{\"id\": 8, \"size\": 10, \"x\": 7, "
                         "\"y\": 2}, {\"id\": 9, \"size\": 2, \"x\": 4, "
                         "\"y\": 0}]", output.strip("\n"))

    def test_square_from_json_string_method_with_none_parameter(self):
        """Check that from_json_string returns an empty list for None Parameter
        """
        output = Square.from_json_string(json_string=None)
        self.assertEqual([], output)

    def test_square_from_json_string_method_with_empty_list_parameter(self):
        """Check that from_json_string returns an empty list for None Parameter
        """
        output = Square.from_json_string("")
        self.assertEqual([], output)

    def test_square_from_json_string_with_appropriate_parameter(self):
        """Check that from_json_string returns an empty list for None Parameter
        """
        json_input = ('[{"id": 89, "width": 10, "height": 4}, '
                      '{"id": 7, "width": 1, "height": 7}]')
        output = Square.from_json_string(json_input)
        self.assertEqual([{'id': 89, 'width': 10, 'height': 4},
                          {'id': 7, 'width': 1, 'height': 7}], output)

    def test_square_create_with_None_parameter(self):
        """Check that create method  works
        """
        dict_1 = {'id': 1}
        sqr_1 = Square.create(**dict_1)

        dict_2 = {'id': 2, 'size': 10}
        sqr_2 = Square.create(**dict_2)

        dict_3 = {'id': 3, 'size': 10, 'x': 7}
        sqr_3 = Square.create(**dict_3)

        dict_4 = {'id': 3, 'size': 10, 'x': 7, 'y': 9}
        sqr_4 = Square.create(**dict_4)

        self.assertEqual(sqr_1.id, dict_1["id"])
        self.assertEqual(sqr_2.id, dict_2["id"])
        self.assertEqual(sqr_2.size, dict_2["size"])
        self.assertEqual(sqr_3.id, dict_3["id"])
        self.assertEqual(sqr_3.size, dict_3["size"])
        self.assertEqual(sqr_3.x, dict_3["x"])
        self.assertEqual(sqr_4.id, dict_4["id"])
        self.assertEqual(sqr_4.size, dict_4["size"])
        self.assertEqual(sqr_4.x, dict_4["x"])
        self.assertEqual(sqr_4.y, dict_4["y"])

    def test_square_load_from_file_returns_empty_list(self):
        """This test loads from a file
        """
        filename = "Square.json"
        os.rename(filename, "Rect.json")
        output = Square.load_from_file()
        self.assertEqual([], output)
        os.rename("Rect.json", filename)

    def test_square_load_from_file_returns_instance_list(self):
        """This test loads from a file for a square
        """
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4, 0, 9)
        Square.save_to_file([r1, r2])
        instance_list = Square.load_from_file()

        self.assertEqual(r1.id, instance_list[0].id)
        self.assertEqual(r1.size, instance_list[0].size)
        self.assertEqual(r2.id, instance_list[1].id)
        self.assertEqual(r2.size, instance_list[1].size)

    def test_square_save_in_csv_empty_list_for_None_parameter(self):
        """Check it saves in CSV format an empty file for None parameter
        """
        Square.save_to_file_csv(None)

        with open("Square.csv", "r", encoding="utf-8") as csv_file:
            output = csv_file.read()

        self.assertEqual("", output.strip("\n"))

    def test_square_save_in_csv_empty_list_for_empty_list_param(self):
        """Check it saves in CSV format an empty file for an empty
        list parameter
        """
        Square.save_to_file_csv([])

        with open("Square.csv", "r", encoding="utf-8") as csv_file:
            output = csv_file.read()

        self.assertEqual("", output.strip("\n"))

    def test_square_save_in_csv_to_file_with_appropriate_params(self):
        """Check it saves in CSV format an empty file for an appropriate
        parameter
        """
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4, 0, 9)
        Square.save_to_file_csv([r1, r2])

        with open("Square.csv", "r", encoding="utf-8") as csv_file:
            output = csv_file.read()

        self.assertEqual("8,10,7,2\n9,2,4,0\n", output)

    def test_square_load_from_file_csv_returns_empty_list(self):
        """This test loads from a csv file
        """
        filename = "Square.csv"
        os.rename(filename, "Sqr.csv")
        output = Square.load_from_file_csv()
        self.assertEqual([], output)
        os.rename("Sqr.csv", filename)

    def test_square_load_from_file_csv_returns_instance_list(self):
        """This test loads from a csv file for a square
        """
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4, 0, 9)
        Square.save_to_file_csv([r1, r2])
        instance_list = Square.load_from_file_csv()

        self.assertEqual(r1.id, instance_list[0].id)
        self.assertEqual(r1.size, instance_list[0].size)
        self.assertEqual(r2.id, instance_list[1].id)
        self.assertEqual(r2.size, instance_list[1].size)
