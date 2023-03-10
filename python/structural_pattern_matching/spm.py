# if-else to match

num: int

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
