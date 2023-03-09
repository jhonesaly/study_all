import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from find_future import *

class TestDateCalculateAge(unittest.TestCase):

    def test_find_fure_found(self):

        input_1 = ['22/4/1233', '1/3/0633', '23/5/5665', '4/12/2330']
        input_2 = ['23/3/4345']
        
        output_actual = find_future(input_1,input_2)    
        output_expected = [datetime.date(5665, 5, 23)]
        
        self.assertEqual(output_actual,output_expected)

        input_1 = ['22/4/1233', '1/3/0633', '23/5/5665', '4/12/2330']
        input_2 = ['23/3/4345', '25/5/1244']
        
        output_actual = find_future(input_1,input_2)
        output_expected = [datetime.date(5665, 5, 23), datetime.date(1233, 4, 22)]
        
        self.assertEqual(output_actual,output_expected)

        input_1 = ['22/4/1233', '1/3/0633', '23/5/5665', '4/12/2330']
        input_2 = ['test','data','inválida']
        
        output_actual = find_future(input_1,input_2)
        output_expected = [-1,-1,-1]
        
        self.assertEqual(output_actual,output_expected)
    
if __name__ == '__main__':
    unittest.main()