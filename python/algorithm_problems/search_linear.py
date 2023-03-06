# Algoritmo:

# 1 Set the first element of the array as the current element.
# 2 If the current element is the target element, return its index.
# 3 If the current element is not the target element and if there are more elements in the array, set the current element to the next element and repeat step 2.
# 4 If the current element is not the target element and there are no more elements in the array, return -1 to indicate that the element was not found.

def search_linear_func(list, val):
    outputx = -1
    
    for num in list:
        if num == val:
            outputx = list.index(val)
    
    return outputx

# Bibliotecas:

import os

# Dados estáticos:

list = [0, 20, 80, 30, 60, 50, 110, 100, 130, 170]

# Software:

os.system('cls')

def search_linear_continuous(list, val):
    while exit != True:

        outputx = -1 

        # Entrada de dados:

        inputx = input('Digite "exit" para sair ou o número a ser buscado: ')

        # Tratamento dos dados:

        if inputx.isnumeric():
            try:
                inputx = int(inputx)
            except:
                os.system('cls')
                print('digite um número inteiro')

        elif inputx == 'exit':
            os.system('cls')
            print('até a próxima!')
            exit = True

        # Operação dos dados:

        outputx = search_linear_func(list, val)

        # Saída dos dados: 

        if outputx != -1:
            os.system('cls')
            print(f'o número faz parte da lista! Sua posição na memória é {outputx}')
        
        else:
            os.system('cls')
            print('o número não faz parte da lista!')
