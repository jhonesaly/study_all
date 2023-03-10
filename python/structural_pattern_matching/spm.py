# if-else spm

num = 1

match num:
    case 1:
        print("um")
    case 2:
        print("dois")
    case _:
        print("outro número")

# Advanced if-else spm

lista = [1, 2, 3]

match lista:
    case [1, 2]:
        print("um e dois")
    case [3, _]:
        print("três e algum outro valor")
    case _:
        print("outros valores")

# Or spm

valor = "b"

match valor:
    case "a" | "b":
        print("valor é 'a' ou 'b'")
    case "c" | "d":
        print("valor é 'c' ou'd'")
    case _:
        print("outro valor")

