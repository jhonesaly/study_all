import unittest
import sys
sys.path.insert(0, 'C:/Users/Cougar_Gamer/Desktop/dev_lif/study_all/python/algorithm_problems')
from search_binary import *

class TestSearchLinear(unittest.TestCase):

    def test_search_binary_found(self):
        self.assertEqual(search_binary_func(test_list, 0), 0)
        self.assertEqual(search_binary_func(test_list, 30), 2)
        self.assertEqual(search_binary_func(test_list, 110), 4)
        self.assertEqual(search_binary_func(test_list, 170), 6)

    def test_search_binary_not_found(self):
        self.assertEqual(search_binary_func(test_list, 40), -1)
        self.assertEqual(search_binary_func(test_list, 90), -1)
        self.assertEqual(search_binary_func(test_list, 120), -1)
        self.assertEqual(search_binary_func(test_list, 200), -1)

if __name__ == '__main__':
    test_list = [0, 20, 30, 60, 110, 130, 170]
    unittest.main()
    exit = True