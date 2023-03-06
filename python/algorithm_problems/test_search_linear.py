import unittest
from search_linear import *

class TestSearchLinear(unittest.TestCase):

    def test_search_linear_found(self):
        self.assertEqual(search_linear(list, 80), 2)
        self.assertEqual(search_linear(list, 30), 3)
        self.assertEqual(search_linear(list, 110), 6)
        self.assertEqual(search_linear(list, 170), 9)

    def test_search_linear_not_found(self):
        self.assertEqual(search_linear(list, 40), -1)
        self.assertEqual(search_linear(list, 90), -1)
        self.assertEqual(search_linear(list, 120), -1)
        self.assertEqual(search_linear(list, 200), -1)

if __name__ == '__main__':
    unittest.main()