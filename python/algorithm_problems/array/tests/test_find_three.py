import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from find_three import *

class TestFindThree(unittest.TestCase):

    def test_find_three_equal(self):
        self.assertEqual(find_three(test_input), test_answer)
    
    def test_array_find_three_notequal(self):
        self.assertNotEqual(find_three(test_input), test_not_answer)

if __name__ == '__main__':
    test_input = {9,8,7,2,1,0}
    test_answer = {9,8,7}
    test_not_answer = {0,1,2}
    unittest.main()
    exit = True