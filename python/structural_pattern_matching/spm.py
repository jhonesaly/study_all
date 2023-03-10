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

# Case guard

valor = 7

match valor:
    case x if x < 5:
        print("valor é menor que 5")
    case x if x > 10:
        print("valor é maior que 10")
    case _:
        print("valor é entre 5 e 10, inclusive")

