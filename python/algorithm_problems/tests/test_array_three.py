import unittest
import sys
sys.path.insert(0, 'C:/Users/Cougar_Gamer/Desktop/dev_lif/study_all/python/algorithm_problems')
from array_find_three import *

class TestSearchLinear(unittest.TestCase):

    def test_array_find_three_equal(self):
        self.assertEqual(array_find_three_func(test_input), test_answer)
    
    def test_array_find_three_notequal(self):
        self.assertNotEqual(array_find_three_func(test_input), test_not_answer)

if __name__ == '__main__':
    test_input = {9,8,7,2,1,0}
    test_answer = {9,8,7}
    test_not_answer = {0,1,2}
    unittest.main()
    exit = True