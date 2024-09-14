#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_orderded_list(self):
        test_list = [1, 2, 3, 4]
        expected_value = 4
        self.assertEqual(max_integer(test_list), expected_value)

    def test_unorderded_list(self):
        test_list = [2, 4, 1, 3]
        expected_value = 4
        self.assertEqual(max_integer(test_list), expected_value)

    def test_one_element_list(self):
        test_list = [5]
        expected_value = 5
        self.assertEqual(max_integer(test_list), expected_value)

    def test_empty_list(self):
        test_list = []
        expected_value = None
        self.assertEqual(max_integer(test_list), expected_value)

    def test_max_at_the_beginning(self):
        test_list = [4, 2, 1, 3]
        expected_value = 4
        self.assertEqual(max_integer(test_list), expected_value)

    def test_one_negative_number_list(self):
        test_list = [-4, 2, 1, 3]
        expected_value = 3
        self.assertEqual(max_integer(test_list), expected_value)

    def test_one_negative_number_list(self):
        test_list = [-4, 2, 1, 3]
        expected_value = 3
        self.assertEqual(max_integer(test_list), expected_value)

    def test_only_negative_number_list(self):
        test_list = [-4, -2, -1, -3]
        expected_value = -1
        self.assertEqual(max_integer(test_list), expected_value)
