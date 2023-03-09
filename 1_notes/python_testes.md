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

## Unittest

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

Para fazer vários testes do mesmo tipo de uma vez:

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

Para fazer tete de erro:

    def test_soma_sem_a_int_ou_float_retorna_erro(self):
        with self.assertRaises(AssertionError):
            soma('11',0)

    def test_soma_sem_b_int_ou_float_retorna_erro(self):
        with self.assertRaises(AssertionError):
            soma(2,'4')

    def test_soma_sem_a_int_ou_float_retorna_erro(self):
        with self.assertRaises(AssertionError):
            soma('11',0)

    def test_soma_sem_b_int_ou_float_retorna_erro(self):
        with self.assertRaises(AssertionError):
            soma(2,'4')

Para se executar todos os testes presentes na pasta atual, se utilzia o comando:

    python -m unittest -v

Caso os arquivos de testes estejam situados em outra pasta, é necessário adicioná-los ao path do interpretador por meio de:

    try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../tests'
            )
        )
    )

## Coverage

Fazer o teste de cobertura é uma maneira importante de garantir que seu código Python esteja testado adequadamente. Existem várias ferramentas para medir a cobertura de código em Python, mas um dos mais populares é o coverage.py. Neste tutorial, vou explicar como usá-lo para testar sua cobertura de código em Python.

Antes de começar, você precisará instalar o coverage.py. A maneira mais fácil de fazer isso é usar o pip, o gerenciador de pacotes padrão do Python. Abra o terminal e digite o seguinte comando:

    pip install coverage

Isso instalará o coverage.py e suas dependências.

Para começar a usar o coverage.py, você precisa criar um arquivo de configuração. Crie um arquivo chamado .coveragerc na raiz do seu projeto e adicione o seguinte conteúdo:

    [run]
    source = .
    omit = */tests/*

    [report]
    show_missing = True

O parâmetro source indica a pasta em que o coverage.py deve procurar pelo código a ser testado. Neste caso, estamos dizendo para procurar em todas as pastas do projeto. O parâmetro omit exclui as pastas que contêm arquivos de teste. Isso significa que o coverage.py não incluirá o código de teste em sua medição de cobertura. O parâmetro show_missing indica que o coverage.py deve mostrar as linhas que não foram testadas.

Antes de medir a cobertura do seu código, você precisa escrever os testes. Para este tutorial, vamos criar um simples programa que calcula a área de um círculo. Crie um arquivo chamado circle.py e adicione o seguinte código:

    import math

    def area(radius):
        return math.pi * radius ** 2

Este é o código que queremos testar. Agora, crie um arquivo chamado test_circle.py e adicione o seguinte código:

    import unittest
    import circle

    class TestCircle(unittest.TestCase):

        def test_area(self):
            self.assertEqual(circle.area(1), math.pi)
            self.assertEqual(circle.area(2.5), math.pi * 2.5 ** 2)

Este é um teste simples que verifica se a função area retorna o valor correto para diferentes raios.

Agora que temos os testes, podemos medir a cobertura do código. Abra o terminal e digite o seguinte comando:

    coverage run --source=. -m unittest discover

Este comando usa o coverage.py para executar os testes em seu projeto e medir a cobertura de código. O parâmetro --source diz ao coverage.py para medir apenas o código em sua pasta atual. O parâmetro -m unittest discover executa todos os testes em seu projeto.

Depois de executar o coverage.py, você pode gerar um relatório da cobertura de código. Para gerar um relatório em HTML, digite o seguinte comando:

    coverage html

Este comando gera um relatório em HTML na pasta htmlcov. Abra o arquivo htmlcov/index.html em seu navegador para ver o relatório completo da cobertura de código.

O relatório de cobertura exibe informações sobre cada arquivo Python no projeto e quantas linhas foram executadas durante a execução dos testes. Ele também mostra as linhas que não foram executadas durante os testes.

Além disso, você pode executar o seguinte comando para exibir um relatório simples no terminal:

    coverage report

Este comando exibe um resumo da cobertura de código em seu terminal, mostrando o percentual de linhas executadas para cada arquivo Python em seu projeto.

------

## TDD

O TDD (Desenvolvimento Orientado a Testes) é uma prática de desenvolvimento de software que enfatiza a escrita de testes antes de escrever o código de produção. Em Python, o TDD é suportado por várias bibliotecas de testes, sendo a mais comum a unittest.

O processo de TDD geralmente segue as seguintes etapas:

- o primeiro passo é escrever um teste que valide o comportamento esperado do código. Este teste deve falhar inicialmente, pois o código de produção ainda não foi escrito.
- após escrever o teste, o próximo passo é escrever o código mínimo necessário para fazê-lo passar. Isso significa que o código deve ser escrito de forma incremental e testado a cada passo.
- uma vez que o teste tenha passado, é hora de refatorar o código para melhorar sua qualidade e legibilidade.
- o processo é então repetido para o próximo teste, e assim por diante, até que todos os requisitos do software tenham sido atendidos.

O Python oferece suporte nativo para testes com a biblioteca unittest, que permite escrever e executar testes unitários, de integração e funcionais. Outras bibliotecas populares para TDD em Python incluem pytest e nose.

Em resumo, TDD é uma prática de desenvolvimento que ajuda a garantir que o código seja testado e funcionando corretamente desde o início. Em Python, é suportado por várias bibliotecas de testes, e a prática pode levar a um código mais seguro, limpo e de fácil manutenção.