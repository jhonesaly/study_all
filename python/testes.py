# Testes com python

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


# try:
#     print(soma('15', 15))

# except AssertionError as e:
#     print(f'Conta inválida: {e}')

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
