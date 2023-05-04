hash = [['','',''],['','',''],['','','']]
end_game = False

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

def move(hash, move):
    move_test = 'not_ok'

    while move_test != 'ok':
        move = move.split(',')
        move = [int(x)-1 for x in move]
        if hash[move[0]][move[1]] != '':
            print('Espaço já marcado. Escolha outro!')
        else:
            hash[move[0]][move[1]] = 'X'
            move_test = 'ok'

while end_game == False:

    for line in hash:
        print(line)
    
    move1_test = 'not_ok'

    while move1_test != 'ok':
        move1 = input("Digite onde deja colocar o X (ex: 1,1): ")
        move1 = move1.split(',')
        move1 = [int(x)-1 for x in move1]
        if hash[move1[0]][move1[1]] != '':
            print('Espaço já marcado. Escolha outro!')
        else:
            hash[move1[0]][move1[1]] = 'X'
            move1_test = 'ok'

    end_game = victory(hash)
    if end_game == True:
        for line in hash:
            print(line)
        break

    move2_test = 'not_ok'

    while move2_test != 'ok':
        move2 = input("Digite onde deja colocar o O (ex: 1,1): ")
        move2 = move2.split(',')
        move2 = [int(x)-1 for x in move2]
        if hash[move2[0]][move2[1]] != '':
            print('Espaço já marcado. Escolha outro!')
        else:
            hash[move2[0]][move2[1]] = 'O'
            move2_test = 'ok'
    
    end_game = victory(hash)
    if end_game == True:
        for line in hash:
            print(line)
        break