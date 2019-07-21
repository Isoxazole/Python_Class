from python_class.Practice_problems.run_empty-1.run import find_pairs
import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(find_pairs([1, 2, 3], 5), [(2, 3), (3, 2)], "Should be True")

    def test_2(self):
        self.assertEqual(find_pairs([1, 2, 3, 4, 5], 8), [(3, 5), (4, 4), (5, 3)], "Should be True")

    def test_3(self):
        self.assertEqual(find_pairs([1, 2, 3], 8), [], "Should be True")

    def test_4(self):
        self.assertEqual(find_pairs([], 8), [], "Should be True")

    # def test_5(self):
    #     with self.assertRaises(AssertionError):
    #         find_pairs([], "hello")
    #
    #     with self.assertRaises(AssertionError):
    #         find_pairs("hello", 9)



if __name__ == '__main__':
    unittest.main()
