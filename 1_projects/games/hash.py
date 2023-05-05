def show_board(board):
    for line in board:
        print(line)

def check_victory(board):
    for i in range(3):
        # Checa linhas
        if board[i][0] == board[i][1] == board[i][2] != '':
            return f'victory of {board[i][0]}!'
        # Checa colunas
        if board[0][i] == board[1][i] == board[2][i] != '':
            return f'victory of {board[0][i]}!'
    # Checa diagonais
    if board[0][0] == board[1][1] == board[2][2] != '':
        return f'victory of {board[0][0]}!'
    if board[0][2] == board[1][1] == board[2][0] != '':
        return f'victory of {board[0][2]}!'
    return ''

def make_move(board, player):
    while True:
        move = input(f"Digite onde desea colocar o {player} (ex: 1,1): ")
        try:
            x, y = [int(i) - 1 for i in move.split(',')]
        except ValueError:
            print('Entrada inválida. Digite novamente.')
            continue
        if board[x][y] != '':
            print('Espaço já marcado. Escolha outro!')
        else:
            board[x][y] = player
            break

board = [['', '', ''], ['', '', ''], ['', '', '']]

while True:
    show_board(board)
    make_move(board, 'X')
    result = check_victory(board)
    if result:
        print(result)
        show_board(board)
        break
    make_move(board, 'O')
    result = check_victory(board)
    if result:
        print(result)
        show_board(board)
        break
