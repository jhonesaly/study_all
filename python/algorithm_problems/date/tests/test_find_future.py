import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from find_future import *

class TestDateCalculateAge(unittest.TestCase):

    def test_find_fure_found(self):
        self.assertEqual(find_future(['22/4/1233', '1/3/0633', '23/5/5665', '4/12/2330'],['23/3/4345', '25/5/1244']),[datetime.date(5665, 5, 23), datetime.date(1233, 4, 22)])

if __name__ == '__main__':
    unittest.main()