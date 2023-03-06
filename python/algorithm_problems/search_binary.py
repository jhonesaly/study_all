# Algoritmo:

# 1 Sort the array in ascending order.
# 2 Set the low index to the first element of the array and the high index to the last element.
# 3 Set the middle index to the average of the low and high indices.
# 4 If the element at the middle index is the target element, return the middle index.
# 5 If the target element is less than the element at the middle index, set the high index to the middle index – 1.
# 6 If the target element is greater than the element at the middle index, set the low index to the middle index + 1.
# 7 Repeat steps 3-6 until the element is found or it is clear that the element is not present in the array.

import os
import sys
sys.path.insert(0, 'C:/Users/Cougar_Gamer/Desktop/dev_lif/study_all/python/algorithm_problems/modules')
from modules.search import *

# Criando dados:

list = gen_rand_list(10, 99)

def search_binary_func(list,search):

    default(list)
    list_size = len(list)
    index_sup = list_size-1
    index_inf = 0
    index_mid = calc_mid_index(index_inf, index_sup)
    
    while (index_sup - index_inf) > 1:
    
        if search == list[index_mid]:
            break

        elif search > list[index_mid]:
            index_inf = index_mid
            index_mid = calc_mid_index(index_inf, index_sup)
            
        elif search < list[index_mid]:
            index_sup = index_mid
            index_mid = calc_mid_index(index_inf, index_sup)
            
    if search == list[index_mid]:
        answer = list[index_mid]
        found(index_mid)
    
    elif search == list[index_inf]:
        answer = list[index_inf]
        found(index_inf)

    elif search == list[index_sup]:
        answer = list[index_sup]
        found(index_sup)

    else:
        answer = -1
    
    return answer

# Iniciando programa

def search_binary_continuous(list,search):

    exit = False

    while exit != True:

        os.system('cls')

        print(f'a lista é: {list}')
        default(list)

        search = input('Digite o número a ser procurado: ')

        if search == 'exit':
            exit = True
            break

        else:
            search = int(search)
        
        answer = search_binary_func(list,search)


        if answer != -1:
            found(answer)
        
        else:
            os.system('cls')
            print('O número procurado não está na lista!')

search_binary_func(list,2)
