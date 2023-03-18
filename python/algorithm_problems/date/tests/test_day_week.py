import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from day_week import *

class TestDateDayWeek(unittest.TestCase):

    def test_day_week_found(self):
        input_1 = '18/3/2023'
        output_actual = day_week(input_1)    
        output_expected = 7
        
        self.assertEqual(output_actual,output_expected)

        input_1 = '19/3/2023'
        output_actual = day_week(input_1)    
        output_expected = 1
        
        self.assertEqual(output_actual,output_expected)

        input_1 = '17/3/2023'
        output_actual = day_week(input_1)    
        output_expected = 6
        
        self.assertEqual(output_actual,output_expected)

if __name__ == '__main__':
    unittest.main()