import unittest
import sys
sys.path.insert(0, 'C:/Users/Cougar_Gamer/Desktop/dev_lif/study_all/python/algorithm_problems')
from search_linear import *

class TestSearchLinear(unittest.TestCase):

    def test_search_linear_found(self):
        self.assertEqual(search_linear_func(list, 80), 2)
        self.assertEqual(search_linear_func(list, 30), 3)
        self.assertEqual(search_linear_func(list, 110), 6)
        self.assertEqual(search_linear_func(list, 170), 9)

    def test_search_linear_not_found(self):
        self.assertEqual(search_linear_func(list, 40), -1)
        self.assertEqual(search_linear_func(list, 90), -1)
        self.assertEqual(search_linear_func(list, 120), -1)
        self.assertEqual(search_linear_func(list, 200), -1)

if __name__ == '__main__':
    unittest.main()
    exit = True