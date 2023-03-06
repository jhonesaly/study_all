import unittest
import sys
sys.path.insert(0, 'C:/Users/Cougar_Gamer/Desktop/dev_lif/study_all/python/algorithm_problems')
from array_find_three import *

class TestSearchLinear(unittest.TestCase):

    def test_array_find_three(self):
        self.assertIn({10,9,8}, test_input)
        self.assertEqual(array_find_three_func(test_input), {10,9,8})
        self.assertNotEqual(array_find_three_func(test_input), {1,2,3})

if __name__ == '__main__':
    test_input = [9,8,7,6,5,4,3,2,1,0]
    unittest.main()
    exit = True