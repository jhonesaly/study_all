import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sum_minute import *

class TestDateSumMinute(unittest.TestCase):
    def test_sum_minute_basic(self):
        self.assertEqual(sum_minute('12:43', 21),'13:04')
        self.assertEqual(sum_minute('20:39', 534),'05:33')
    
if __name__ == '__main__':
    unittest.main()