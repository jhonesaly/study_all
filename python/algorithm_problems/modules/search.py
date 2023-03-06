import os
import random

# Criando funções

## Criando lista de dados

def gen_rand_list(list_range, lim_sup, lim_inf=0):
    # modo alternativo: list = random.sample(range(list_range), list_size)    
    
    list = []
    for num in range(list_range):
        num = random.randint(lim_inf, lim_sup)
        list.append(num)
    list.sort()
    return list

## Calculando o index do meio
 
def calc_mid_index(index_inf, index_sup):
    mid_index = int((index_inf + index_sup)/2)
    return mid_index

## Definindo variáveis de busca

def default(list):
    global list_size, index_sup, index_inf, index_mid
    list_size = len(list)
    index_sup = list_size-1
    index_inf = 0
    index_mid = calc_mid_index(index_inf, index_sup)
    return list_size, index_sup, index_inf, index_mid

## Valor encontrado

def found(index):
    os.system('cls')
    print('O número está na lista!')
    print(f'O index do número é: {index}')