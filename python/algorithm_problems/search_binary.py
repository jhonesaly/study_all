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

sys.path.insert(0, 'C:/Users/Cougar_Gamer/Desktop/dev_lif/study_all/python/algorithm_problems/modules/search.py')
from modules.search import *

# Criando dados:

def search_binary_func(list,search):

    list_size, index_sup, index_inf, index_mid = default(list)
    
    while (index_sup - index_inf) > 1:
    
        mid = list[index_mid]
        inf = list[index_inf]
        sup = list[index_sup]
    
        if search == mid:
            break

        elif search > mid:
            index_inf = index_mid
            index_mid = calc_mid_index(index_inf, index_sup)
            
        elif search < mid:
            index_sup = index_mid
            index_mid = calc_mid_index(index_inf, index_sup)
            
    if search == mid:
        index = index_mid
        found(index_mid)
    
    elif search == inf:
        index = index_inf
        found(index_inf)

    elif search == sup:
        index = index_sup
        found(index_sup)

    else:
        index = -1
    
    return index

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


test_list = [0, 20, 30, 60, 110, 130, 170]
answer = search_binary_func(test_list,130)
print(answer)