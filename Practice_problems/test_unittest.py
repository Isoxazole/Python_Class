from python_class.Practice_problems import run_empty
import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(string_rotation('ABC', 'BCA'), True, "Should be True")

    def test_2(self):
        self.assertEqual(string_rotation('ABC', "CAB"), True, "Should be True")

    def test_3(self):
        self.assertEqual(string_rotation('ABC', "CBA"), False, "Should be False")

    def test_4(self):
        self.assertEqual(string_rotation('ABCDEFG', "BCDEFGA"), True, "Should be False")

    def test_5(self):
        self.assertEqual(string_rotation('Default string', 'Another string'), False, "Should be True")

    def test_6(self):
        self.assertEqual(string_rotation('Default string', 'A larger string'), False, "Should be True")

    # def test_7(self):
    #     with self.assertRaises(AssertionError):
    #         string_rotation("ABC", 9)
    #
    #     with self.assertRaises(AssertionError):
    #         string_rotation(9, "ABC")

if __name__ == '__main__':
    unittest.main()

