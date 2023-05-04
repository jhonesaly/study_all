hash = [['','',''],['','',''],['','','']]
end_game = False

def show(hash):
    for line in hash:
        print(line)

def victory(hash):
    end_game = False

    for x in range(2):
        if hash[x][0] == hash[x][1] == hash[x][2]:
            if hash[x][0] != '':
                print(f'victory of {hash[x][0]}!')
                end_game = True
                break
    
        elif hash[0][x] == hash[1][x] == hash[2][x]:
            if hash[0][x] != '':
                print(f'victory of {hash[0][x]}!')
                end_game = True
                break

        elif (hash[0][0] == hash[1][1] == hash[2][2]):
            if hash[1][1] != '':
                print(f'victory of {hash[1][1]}!')
                end_game = True
                break

        elif (x==0) and (hash[0][2] == hash[1][1] == hash[2][0]):
            if hash[x+1][x+1] != '':
                print(f'victory of {hash[1][1]}!')
                end_game = True
                break

        else:
            continue
    
    return end_game

def move(hash, XO):
    move_test = 'not_ok'

    while move_test != 'ok':
        move = input(f"Digite onde deja colocar o {XO} (ex: 1,1): ")
        move = move.split(',')
        move = [int(x)-1 for x in move]
        if hash[move[0]][move[1]] != '':
            print('Espaço já marcado. Escolha outro!')
        else:
            hash[move[0]][move[1]] = XO
            move_test = 'ok'

while end_game == False:

    show(hash)

    move(hash,'X')

    end_game = victory(hash)

    if end_game == True:
        show(hash)
        break

    move(hash,'O')
    
    end_game = victory(hash)
    
    if end_game == True:
        show(hash)
        break