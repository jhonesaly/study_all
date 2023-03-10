import unittest
import os
import sys
import coverage

cov = coverage.Coverage()
cov.start()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sum_minute import *

class TestDateSumMinute(unittest.TestCase):
    def test_sum_minute_basic(self):
        self.assertEqual(sum_minute('12:43', 21),'13:04')
        self.assertEqual(sum_minute('20:39', 534),'05:33')
    
    def test_sum_minute_arg2_is_str(self):
        self.assertEqual(sum_minute('12:43', '21'),'13:04')
        self.assertEqual(sum_minute('20:39', '534'),'05:33')
    
    def test_sum_minute_arg2_invalid(self):
        with self.assertRaises(ValueError):
            sum_minute('12:43', 'abc')

cov.stop()
cov.save()
cov.report()

if __name__ == '__main__':
    unittest.main()