import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from positive_negative import *

class TestPositiveNegative(unittest.TestCase):
    def test_positive_negative_equal(self):
        result_1 = positive_negative(test_input_1)
        self.assertEqual(result_1, test_answer_1)
    
    def test_more_positive(self):
        result_2 = positive_negative(test_input_2)
        self.assertEqual(result_2, test_answer_2)

    def test_more_negative(self):
        result_3 = positive_negative(test_input_3)
        self.assertEqual(result_3, test_answer_3)

if __name__ == '__main__':
    
    test_input_1 = [-1, 3, -5, 6, 3, 6, -7, -4, -9, 10]
    test_answer_1 = [3, -1, 6, -5, 3, -7, 6, -4, 10, -9]

    test_input_2 = [-1, 3, -5, 6, 3, 6, -7, -4, -9, 10, 11, 12, 13]
    test_answer_2 = [3, -1, 6, -5, 3, -7, 6, -4, 10, -9 , 11, 12, 13]

    test_input_3 = [-1, 3, -5, 6, 3, 6, -7, -4, -9, 10, -11, -12, -13]
    test_answer_3 = [3, -1, 6, -5, 3, -7, 6, -4, 10, -9 , -11, -12, -13]

    unittest.main()