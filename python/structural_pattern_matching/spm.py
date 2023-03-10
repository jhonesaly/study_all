# if-else to match

num = 1

if num == 1:
    print("um")
elif num == 2:
    print("dois")
else:
    print("outro número")

match num:
    case 1:
        print("um")
    case 2:
        print("dois")
    case _:
        print("outro número")

# Advanced if-else spm

lista = [1, 2]

match lista:
    case [1, 2]:
        print("um e dois")
    case [3, _]:
        print("três e algum outro valor")
    case _:
        print("outros valores")

