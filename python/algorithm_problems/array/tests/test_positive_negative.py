import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from positive_negative import *

class TestPositiveNegative(unittest.TestCase):
    def test_positive_negative_equal(self):
        result_1 = positive_negative(test_input_1)
        self.assertEqual(result_1, test_answer_1)

if __name__ == '__main__':
    
    test_input_1 = [-1, 3, -5, 6, 3, 6, -7, -4, -9, 10]
    test_answer_1 = [3, -1, 6, -5, 3, -7, 6, -4, 10, -9]

    unittest.main()