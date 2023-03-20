import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from reorder import *

class TestReorder(unittest.TestCase):
    def test_reorder_equal(self):
        result_1, result_2 = reorder(test_input_1, test_input_2)
        self.assertEqual(result_1, test_answer_1)
        self.assertEqual(result_2, test_answer_2)
    
    def test_reorder_notequal(self):
        result_1, result_2 = reorder(test_input_1, test_input_2)
        self.assertNotEqual(result_1, test_not_answer_1)
        self.assertNotEqual(result_2, test_not_answer_2)

    def test_reorder_same_length(self):
        self.assertEqual(len(test_input_1), len(test_input_1))
    
    def test_positive_negative_not_same_length(self):
        self.assertNotEqual(len(test_input_1), len(test_input_3))
    

if __name__ == '__main__':
    test_input_1 = [10, 11, 12]
    test_input_2 = [1, 0, 2]
    test_input_3 = [12, 15, 16, 20]

    test_answer_1 = [11, 10, 12]
    test_answer_2 = [0, 1, 2]

    test_not_answer_1 = [10, 11, 12]
    test_not_answer_2 = [1, 0, 2]
    unittest.main()