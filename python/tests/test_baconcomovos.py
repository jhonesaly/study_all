"""
TDD

RED: Criar o teste e ver falhar

GREEN: Criar o código e ver passar

REFACTOR: Melhorar código

"""
import unittest
import os
from baconcomovos import bacon_com_ovos

os.system('cls')

class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_assertion_error_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('')
    
    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada), 
                    saida,
                    msg=f'\n\n{entrada} não retornou {saida}'
                )

if __name__ == '__main__':
    unittest.main(verbosity=2)