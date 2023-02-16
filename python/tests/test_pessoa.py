"""
class Pessoa
    __init__
        nome str
        sobrenome str
        dados_obtidos bool

    API:
        obter_todos_os_dados -> method
            OK
            404
"""
import unittest

class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa('Luiz', 'Otávio')



if __name__ == "__main__":
    unittest.main(verbosity=2)
else:
    unittest.main()