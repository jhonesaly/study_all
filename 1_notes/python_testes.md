# Testes com python

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

