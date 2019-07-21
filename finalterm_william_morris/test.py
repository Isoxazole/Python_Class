"""
This file contains tests for finding pictures of cities.
Tests here to see if program checks for valid cities or not
"""


from python_class.finalterm_william_morris.run import get_city_image_url
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_city_image_url("Barcelona"), "Should be True")
    def test_2(self):
        self.assertEqual(get_city_image_url("tomato"), "Should be False")