"""
TDD

RED: Criar o teste e ver falhar

GREEN: Criar o código e ver passar

REFACTOR: Melhorar código

"""
import unittest


class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos(0)

unittest.main(verbosity=2)