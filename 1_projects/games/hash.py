hash = ['','',''],['','',''],['','','']

end_game = False

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
    
    # victory

    for x in range(2):
        if hash[x][0] == hash[x][1] == hash[x][2]:
            print(f'victory of {hash[x][0]}!')
            end_game = True
    
        elif hash[0][x] == hash[1][x] == hash[2][x]:
            print(f'victory of {hash[0][x]}!')
            end_game = True
