import unittest
import sys
sys.path.insert(0, 'C:/Users/Cougar_Gamer/Desktop/dev_lif/study_all/python/algorithm_problems')
from search_binary import *

class TestSearchLinear(unittest.TestCase):

    def test_search_binary_found(self):
        self.assertEqual(search_binary_func(test_list, 80), 2)
        self.assertEqual(search_binary_func(test_list, 30), 3)
        self.assertEqual(search_binary_func(test_list, 110), 6)
        self.assertEqual(search_binary_func(test_list, 170), 9)

    def test_search_binary_not_found(self):
        self.assertEqual(search_binary_func(test_list, 40), -1)
        self.assertEqual(search_binary_func(test_list, 90), -1)
        self.assertEqual(search_binary_func(test_list, 120), -1)
        self.assertEqual(search_binary_func(test_list, 200), -1)

if __name__ == '__main__':
    test_list = [0, 20, 80, 30, 60, 50, 110, 100, 130, 170]
    unittest.main()
    exit = True