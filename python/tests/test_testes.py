import unittest
from testes import soma

class TestTestes(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5,5), 10)

    def test_varias_entradas(self):
        a_b_saidas = (
            (10, 10, 20),
            (10, 15, 25),
            (20, 25, 45),
            (20, 20, 40),           
        )

        for a_b_saida in a_b_saidas:
            with self.subTest(a_b_saida=a_b_saida):
                a, b, saida = a_b_saida
                self.assertEqual(soma(a,b), saida)

    def test_soma_sem_a_int_ou_float_retorna_erro(self):
        with self.assertRaises(AssertionError):
            soma('11',0)

    def test_soma_sem_b_int_ou_float_retorna_erro(self):
        with self.assertRaises(AssertionError):
            soma(2,'4')


if __name__ == "__main__":
    unittest.main(verbosity=2)