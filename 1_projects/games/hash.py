hash = ['','',''],['','',''],['','','']

end_game = False

while end_game == False:

    for line in hash:
        print(line)
    
    move1 = input("Digite onde deja colocar o X (ex: 1,1): ")
    move2 = input("Digite onde deja colocar o O (ex: 1,1): ")

    move1 = move1.split(',')
    move1 = [int(x)-1 for x in move1]
    hash[move1[0]][move1[1]] = 'X'
        
    end_game = True

    print(hash[0][0])
    print(move1[0])