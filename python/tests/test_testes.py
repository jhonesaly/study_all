import unittest
from testes import soma

class TestTestes(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5,5), 10)

    def test_varias_entradas(self):
        a_b_saidas = (
            (10, 10, 20)
            (10, 10, 11)
            (5, 5, 10)
            (1, 1, 3)
            
        )
    
unittest.main(verbosity=2)