import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from positive_negative import *

class TestPositiveNegative(unittest.TestCase):
    def test_positive_negative_equal(self):
        result_1, result_2 = positive_negative(test_input_1, test_input_2)
        self.assertEqual(result_1, test_answer_1)
        self.assertEqual(result_2, test_answer_2)
    

if __name__ == '__main__':
    test_input_1 = [10, 11, 12]
    test_input_2 = [1, 0, 2]

    test_answer_1 = [11, 10, 12]
    test_answer_2 = [0, 1, 2]

    #test_not_answer = 
    unittest.main()