#!/usr/bin/python3
"""This module runs a unittest on the Base Model Class created
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """This is the test case for testing the functionality
    of the Base Model Class
    """

    def setUp(self):
        """Setup Base Class for each instance
        """
        self.base_class_1 = Base()
        self.base_class_2 = Base()
        self.base_class_3 = Base(12)
        self.base_class_4 = Base()
        self.base_class_5 = Base(13)

    def tearDown(self):
        """TearDown BaseClass for each instance
        """
        pass

    def test_id_is_present(self):
        """Check if id is present
        """
        self.assertTrue(self.base_class_1.id is not None)
        self.assertTrue(self.base_class_2.id is not None)
        self.assertTrue(self.base_class_3.id is not None)
        self.assertTrue(self.base_class_4.id is not None)

    def test_id_is_not_zero(self):
        """Check if id is not zero
        """
        self.assertTrue(self.base_class_1.id != 0)
        self.assertTrue(self.base_class_2.id != 0)
        self.assertTrue(self.base_class_3.id != 0)
        self.assertTrue(self.base_class_4.id != 0)

    def test_id_is_increasing(self):
        """Check if id is increasing as new base class is created
        """
        self.assertTrue(self.base_class_2.id > self.base_class_1.id)
        self.assertTrue(self.base_class_4.id > self.base_class_1.id)

    def test_id_is_increasing_by_one(self):
        """Check if id is increasing as new base class is created
        by one
        """
        self.assertTrue(self.base_class_2.id - self.base_class_1.id == 1)
        self.assertTrue(self.base_class_4.id - self.base_class_2.id == 1)

    def test_id_is_expected_value(self):
        """Check that the expected value matches the id of instance
        """
        self.assertEqual(self.base_class_3.id, 12)
        self.assertEqual(self.base_class_5.id, 13)

    def test_base_to_json_string_method_returns_str(self):
        """Check if json string return value is string
        """
        dictionary = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        type_json_str = type(Base.to_json_string([dictionary]))
        self.assertTrue(type_json_str is str)

    def test_base_returns_str_rep_of_an_empty_list(self):
        """Check if json returns emptylist string representation
        """
        json_str_1 = Base.to_json_string(None)
        json_str_2 = Base.to_json_string([])

        self.assertEqual(json_str_1, "[]")
        self.assertEqual(json_str_2, "[]")

    def test_base_returns_str_rep_of_list_of_dictionaries(self):
        """Check if json string is the expected value and not empty
        """
        dict_1 = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_str = Base.to_json_string([dict_1])

        self.assertEqual(json_str, ("[{\"x\": 2, \"width\": 10, "
                                    "\"id\": 1, \"height\": 7, \"y\": 8}]"))
