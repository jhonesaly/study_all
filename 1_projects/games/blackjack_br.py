# BLACK JACK - in Python

'''
Regras: O blackjack (modalidade americana) é um jogo de cartas que consiste em somar mais pontos 
com as suas cartas que o dealer sem ultrapassar 21. Se com as 2 primeiras cartas o jogador conseguir 
21 pontos, terá um “blackjack”.

Valor das cartas:

- O “Ás” vale 1 ou 11 pontos, aquilo que for mais vantajoso para o jogador.
- “J”, “Q”, “K” valem 10 pontos.
- As demais cartas, seu próprio valor.

Como jogar o blackjack:

No seu turno, cada jogador tem várias opções sempre e quando não tenha “blackjack”:

- Pedir (hit): O dealer distribui uma carta mais ao jogador. Se as cartas somarem mais de 21 pontos, 
automaticamente perde e passa a vez.

- Parar (stand): O jogador fica com as cartas que tiver e passa a vez ao seguinte jogador.

- Desistir (Quit): O jogador pode desistir antes de realizar qualquer outra ação. Recupera a metade do que apostou.

- Dobrar (double). Um jogador pode dobrar a aposta se tiver 9, 10 ou 11 pontos. Se dobrar, 
o dealer distribuirá uma carta mais ao jogador e terminará o turno.

- Dividir (split). Quando as 2 primeiras cartas tiverem o mesmo valor, poderão ser divididas em 2 jogadas 
independentes e cada uma com a sua própria aposta. Se 2 ases forem divididos, somente é distribuída 
uma carta a cada jogada e o turno se acaba. Não se pode ter “blackjack” depois de dividir.
Nesta modalidade, somente é possível dividir uma única vez.

- Seguro. Quando a carta virada para cima do dealer for um ás, pode-se apostar que o dealer tem blackjack. 
O jogador deve fazer uma aposta adicional com a metade do valor que havia apostado. Esta jogada é decidida
no mesmo instante. Caso acerte, o dealer pagará esta aposta 2 a 1; caso contrário perde-se o seguro e a 
ordem normal do jogo é seguida.
'''

#import time
import random
import os

print(f'{"*"*58} \n Bem-vindo ao cassino game: BLACK JACK (21) ! \n{"*"*58}')

deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
d_cards = []  # cartas do dealer
p_cards = []  # cartas do jogador

dealer_pot = 0 #pontuação do dealer
player_pot = 0  #pontuação do jogador
balance = player_pot - dealer_pot #lucro do jogador

bank = 0 # disponível no banco
bet = 0 # valor da aposta
#timer = 0

exit = False

while not exit:

    #Setting:
    # os.system('cls')
    print(f'Você possui R${bank},00')
    
    choice_1 = input('Deseja [A]postar, fazer [D]epósito ou [S]air? ')
    choice_1 = choice_1.lower()
        
    if choice_1 == 'd':
        
        bank_input = input('Digite quanto deseja depositar (somente valores inteiros): ')

        try:
            bank_transfer = int(bank_input)
            bank += bank_transfer
        
        except:
            print('\nDigite um valor válido.\n')
            continue     
    
    elif choice_1 == 's':
        os.system('cls')
        print('\nObrigado por ter jogado!\n')
        print(f'\nSeu balanço é de R${balance},00\n')
        print('\nAté a próxima!\n')
        print('\nSaindo...\n')
        exit = True
        break
    
    elif choice_1 == 'a':
        
        bet_input = input('Digite quanto deseja apostar (somente valores inteiros): ')
        
        try:
            bet = int(bet_input)
            
            if bet <= bank:
                bank -= bet
            else:
                print('\nAposta maior que valor disponível. Por favor, faça um depósito.\n')
                continue
        
        except:
            print('\nDigite um valor válido.\n')
            continue     

        for i in range(1):
            random.shuffle(deck)
            d_cards.append(deck.pop())
            p_cards.append(deck.pop())

    else:
        print('\nValor inválido. Por favor, tente novamente.\n')
        continue

    #Game





#     print("As cartas do dealer são: X", d_cards[1])
#     print("As cartas do jogador são:", p_cards)

# if sum(p_cards) > 21:
#     print(f"You are BUSTED !\n  {'*'*14}Dealer Wins !!{'*'*14}\n")
#     exit()

# if sum(d_cards) > 21:
#     print(f"Dealer is BUSTED !\n   {'*'*14} You are the Winner !!{'*'*18}\n")
#     exit()

# if sum(d_cards) == 21:
#     print(f"{'*'*24}Dealer is the Winner !!{'*'*14}")
#     exit()

# if sum(d_cards) == 21 and sum(p_cards) == 21:
#     print(f"{'*'*17}The match is tie !!{'*'*25}")
#     exit()


# # function to show the dealer's choice
# def dealer_choice():
#     if sum(d_cards) < 17:
#         while sum(d_cards) < 17:
#             random.shuffle(deck)
#             d_cards.append(deck.pop())

#     print("Dealer has total " + str(sum(d_cards)) + "with the cards ", d_cards)

#     if sum(p_cards) == sum(d_cards):
#         print(f"{'*'*15}The match is tie !!{'*'*15}")
#         exit()

#     if sum(d_cards) == 21:
#         if sum(p_cards) < 21:
#             print(f"{'*'*23}Dealer is the Winner !!{'*'*18}")
#         elif sum(p_cards) == 21:
#             print(f"{'*'*20}There is tie !!{'*'*26}")
#         else:
#             print(f"{'*'*23}Dealer is the Winner !!{'*'*18}")

#     elif sum(d_cards) < 21:
#         if sum(p_cards) < 21 and sum(p_cards) < sum(d_cards):
#             print(f"{'*'*23}Dealer is the Winner !!{'*'*18}")
#         if sum(p_cards) == 21:
#             print(f"{'*'*22}Player is winner !!{'*'*22}")
#         if 21 > sum(p_cards) > sum(d_cards):
#             print(f"{'*'*22}Player is winner !!{'*'*22}")

#     else:
#         if sum(p_cards) < 21:
#             print(f"{'*'*22}Player is winner !!{'*'*22}")
#         elif sum(p_cards) == 21:
#             print(f"{'*'*22}Player is winner !!{'*'*22}")
#         else:
#             print(f"{'*'*23}Dealer is the Winner !!{'*'*18}")


# while sum(p_cards) < 21:

#     # to continue the game again and again !!
#     k = input("Want to hit or stay?\n Press 1 for hit and 0 for stay ")
#     if k == 1:
#         random.shuffle(deck)
#         p_cards.append(deck.pop())
#         print("You have a total of " + str(sum(p_cards)) + " with the cards ", p_cards)
#         if sum(p_cards) > 21:
#             print(f'{"*"*13}You are BUSTED !{"*"*13}\n Dealer Wins !!')
#         if sum(p_cards) == 21:
#             print(f'{"*"*19}You are the Winner !!{"*"*29}')

#     else:
#         dealer_choice()
#         break