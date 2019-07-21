"""
Homework 10, Exercise 2
William Morris
05/05/2019
This program is an example coding interview exercise. Here is the test caes,
the "run_empty.py" file contains the empty function along with the instructions
for the interviewee. The "run.py" file contains the most optimal solution
for this problem
"""


from python_class.HW10.run_empty import reverseWords
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reverseWords("I'll never forget that cake"),
                         "ll'I reven tegrof taht ekac", "Should be True")
    def test_2(self):
        self.assertEqual(reverseWords("Yo, Yo YO,!!:?103"),
                         ",oY oY 301?:!!,OY", "Should be True")
    def test_3(self):
        self.assertEqual(reverseWords(" "), "", "Should be True")
    def test_4(self):
        self.assertEqual(reverseWords("OneBigLongNastyWeirdUglyWord"),
                         "droWylgUdrieWytsaNgnoLgiBenO", "Should be True")
    def test_5(self):
        self.assertEqual(reverseWords("123 456 789"),
                         "321 654 987", "Should be True")

if __name__== '__main__':
    unittest.main()