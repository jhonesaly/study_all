# Testes com python

O trabalho de testes é volumoso, por isso considera-se uma boa prática definir funções que façam apenas uma atividade. Se ela fizer várias coisas, o teste vai ficar excessivamente complexo. Por isso é fundamental modularizar.

## Assertions

A primeira forma de teste é por meio de 'assertions', que são direcionada para o desenvolvedor, não para o usuário final.

    def soma(a, b):
        assert isinstance(a, (int, float)) , 'variável precisa ser int ou float'
        return a + b

rodando o arquivo com a flag [-O] faz as assertions serem desconsideradas, rodando como se elas não existissem.

    python testes.py
    Conta inválida: variável precisa ser int ou float
    
    python -O testes.py
    TypeError: can only concatenate str (not "int") to str

Aqui vai uma lista dos principais tipos de assertion

- assert expression: Verifica se a expressão é verdadeira e, se não for, gera um AssertionError com uma mensagem padrão.
- assert expression, message: Verifica se a expressão é verdadeira e, se não for, gera um AssertionError com a mensagem personalizada fornecida.
- assertEqual(a, b): Verifica se os valores de a e b são iguais.
- assertNotEqual(a, b): Verifica se os valores de a e b são diferentes.
- assertTrue(expression): Verifica se a expressão é verdadeira.
- assertFalse(expression): Verifica se a expressão é falsa.
- assertIn(item, lista): Verifica se o item está na lista.
- assertNotIn(item, lista): Verifica se o item não está na lista.
- assertIs(a, b): Verifica se a é idêntico a b.
- assertIsNot(a, b): Verifica se a não é idêntico a b.
- assertIsNone(expression): Verifica se a expressão é None.
- assertIsNotNone(expression): Verifica se a expressão não é None.
- assertAlmostEqual(a, b): Verifica se os valores de a e b são quase iguais (dentro de uma certa tolerância).
- assertNotAlmostEqual(a, b): Verifica se os valores de a e b não são quase iguais (dentro de uma certa tolerância).
- assertGreater(a, b): Verifica se a é maior que b.
- assertGreaterEqual(a, b): Verifica se a é maior ou igual a b.
- assertLess(a, b): Verifica se a é menor que b.
- assertLessEqual(a, b): Verifica se a é menor ou igual a b.


## Doctests

Veja o seguinte algoritmo:

    def soma(a, b):
        """TEST
        
        >>> soma(5,5)
        11
        
        """
        assert isinstance(a, (int, float)) , 'primeira variável precisa ser int ou float'
        assert isinstance(b, (int, float)) , 'segunda variável precisa ser int ou float'
        return a + b

    if __name__ == '__main__':
        import doctest
        doctest.testmod()

    prompt:

    **********************************************************************
    File "c:\Users\Cougar_Gamer\Desktop\dev_lif\study_all\python\testes.py", 
    line 6, in __main__.soma
    Failed example:
        soma(5,5)
    Expected:
        11
    Got:
        10
    **********************************************************************
    1 items had failures:
    1 of   1 in __main__.soma
    ***Test Failed*** 1 failures.

A primeira coisa a se notar é o 'if' no final, muito comum em vários scripts. Ele é fundamental para para testes porque ele indica que o teste só deve ser realizado se o script estiver sendo executado diretamente. Em geral, os softwares são esritos de maneira modularizada com um script principal que chama os módulos, impedindo que esses testes sejam executados pelo usuário final.

Em segundo lugar, veja que, por meio da biblioteca doctest, aquilo que estiver escrito entre """ será testado, como indicado no código. Aqui foi colocado um resultado esperado errado de propósito para ver uma falha. Se não houver erro, o test não mostrará nada no prompt.

trocando o valor esperado por 10 e colocando como parâmetro no doctest (doctest.testmod(verbose=True)) obtemos o seguinte prompt:

    Trying:      
        soma(5,5)
    Expecting:   
        10       
    ok
    1 items had no tests:      
        __main__
    1 items passed all tests:  
    1 tests in __main__.soma
    1 tests in 2 items.        
    1 passed and 0 failed.     
    Test passed.

Se você já espera um determinado tipo de erro, você pode deixar o "expected" vazio para pegar o retorno do prompt e permitir que esse teste passe.

    def soma(a, b):
    """TEST

        >>> soma('5',5)
        Traceback (most recent call last):
        ...
        AssertionError: primeira variável precisa ser int ou float
        """
        assert isinstance(a, (int, float)) , 'primeira variável precisa ser int ou float'
        assert isinstance(b, (int, float)) , 'segunda variável precisa ser int ou float'
        return a + b

A desvantagem do doctest é que ele fica no mesmo script do algoritmo, o que pode deixá-lo muito grande ou confuso. Por isso recomenda-se usá-lo somente em situações que hajam poucos e simples testes. Para soluções mais complexas, recomenda-se a solução a seguir.

## unittest

Para criar um teste em um script separado, utiliza-se o algoritmo:

    import unittest

    class TestName(unittest.TestCase):
        pass

    unittest.main()

Digamos que agora a soma retorna a + b + 1, vamos executar o seguinte teste:

    class TestTestes(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5,5), 10)
    
    unittest.main(verbosity=2)

o prompt:

    test_soma_5_e_5_deve_retornar_10 (__main__.TestTestes.test_soma_5_e_5_deve_retornar_10) ... FAIL

    ======================================================================
    FAIL: test_soma_5_e_5_deve_retornar_10 (__main__.TestTestes.test_soma_5_e_5_deve_retornar_10)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "c:\Users\Cougar_Gamer\Desktop\dev_lif\study_all\python\tests\test_testes.py", line 6, in test_soma_5_e_5_deve_retornar_10
        self.assertEqual(soma(5,5), 10)
    AssertionError: 11 != 10

    ----------------------------------------------------------------------
    Ran 1 test in 0.002s

