import unittest
import sys
sys.path.insert(0, 'C:/Users/Cougar_Gamer/Desktop/dev_lif/study_all/python/algorithm_problems')
sys.path.insert(0, 'c:/Users/Cougar_Gamer/Documents/GitHub/study_all/python/algorithm_problems')
from date_calculate_age import *

class TestDateCalculateAge(unittest.TestCase):

    def test_date_calculate_age(self):
        self.assertEqual(calculate_age('08/03/2023','08/03/2023'),"a diferença é de 0 anos, 0 meses e 0 dias.")
        self.assertEqual(calculate_age('07/03/2023','08/03/2023'),"a diferença é de 0 anos, 0 meses e 1 dias.")
        self.assertEqual(calculate_age('08/02/2023','08/03/2023'),"a diferença é de 0 anos, 1 meses e 0 dias.")
        self.assertEqual(calculate_age('08/03/2022','08/03/2023'),"a diferença é de 1 anos, 0 meses e 0 dias.")
        self.assertEqual(calculate_age('01/01/2022','08/03/2023'),"a diferença é de 1 anos, 2 meses e 7 dias.")

if __name__ == '__main__':
    unittest.main()