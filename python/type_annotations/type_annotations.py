# variável

uma_string: str = "um, dois, três"
um_inteiro: int = 123
um_float: float = 1.23
um_boolean: bool = True
um_set: set = {1, 2, 3}
uma_lista: list = [1, 2, 3]
uma_tupla: tuple = (1, 2, 3)
um_dicionário: dict = {'um': 1, 'dois': 2, 'três': 3}

uma_string = 'a'
print(uma_string)

# função

def sum(x: int, y: int, z: float) -> float:  
    return x + y + z

soma = sum(1, 2, 3)
print(soma)

# lista

lista_inteiros: list[int] = [1, 2, 3, 4]
lista_strings: list[str] = ["1", "2", "3", "4"]
lista_tuplas: list[tuple] = [(1, "1"), (2, "2")]
lista_listas_int: list[list[int]] = [[1], [4, 5]]

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