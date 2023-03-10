# variável

uma_string: str = "um, dois, três"
um_inteiro: int = 123
um_float: float = 1.23
um_boolean: bool = True
um_set: set = {1, 2, 3}
uma_lista: list = [1, 2, 3]
uma_tupla: tuple = (1, 2, 3)
um_dicionário: dict = {'um': 1, 'dois': 2, 'três': 3}

uma_string = 1
print(uma_string)

# função

def sum(x: int, y: int, z: float) -> float:  
    return x + y + z

soma = sum(1, 2, 3.0)
print(soma)

# listas e sets

lista_inteiros: list[int]
conjunto_strings: set[str]
lista_tuplas: list[tuple] = [(1, "1"), (2, "2")]
lista_listas_int: list[list[int]] = [[1], [4, 5]]

lista_inteiros = ['1']
conjunto_strings = [1]

# dicionário

um_dict: dict[str, int] = {
    "A": 0,
    "B": 0,
    "C": 0,
}

um_dict_de_listas: dict[str, list[int]] = {
    "A": [1, 2],
    "B": [3, 4],
    "C": [5, 6],
}

um_dict = {1: 1, '2': 2.0}
print(um_dict)

# type alias

int_list = list[int]
DictListaInteiros = dict[str, int_list]

um_dict_de_listas: DictListaInteiros = {
    "A": [1, 2],
    "B": [3, 4],
    "C": [5, 6],
}

# type union

string_e_inteiros: str | int
string_e_inteiros = "A"
string_e_inteiros = 2

string_e_inteiros = 2.3

# type option

def sum2(x: int, y: float | None = None) -> float:
    return x + y

sum2(2, 'a')

# type callable

from collections.abc import Callable

def execute_callable(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

def func_callable_format(a: int, b: int) -> int:
    return a + b

def func_not_callable_format(a: float, b: float) -> float:
    return a + b

execute_callable(func_callable_format, 1, 2)
execute_callable(func_not_callable_format, 1.5, 2.5)