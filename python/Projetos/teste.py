# Estatística Básica
import os

l1 = []

while exit != True:
    
    select = input('\nescolha uma das opções: [i]nserir, [m]édia, [exit]\n')

    if select == 'i':

        d1 = input('Entre com os dados: ')
        
        try:
            d1 = int(d1)
            l1.append(d1)
        except:
            print("digite um vor válido")

    elif select == 'm':
        soma = 0

        for i in l1:
            soma += i

        media = soma/len(l1)
        print(f"a media é: {media}")
    
    elif select == 'exit':
        print('Até a próxima')
        exit = True
        break
