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

def sum(x: int, y: int, z: float) -> float:  
    return x + y + z

soma = sum(1, 2, 3)
print(soma)

lista_inteiros: list[int] = [1, 2, 3, 4]
lista_strings: list[str] = ["1", "2", "3", "4"]
lista_tuplas: list[tuple] = [(1, "1"), (2, "2")]
lista_listas_int: list[list[int]] = [[1], [4, 5]]

lista_inteiros: list[int] = [1, 2, 3, 'a']