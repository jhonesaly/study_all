# Algoritmo:

# 1 Sort the array in ascending order.
# 2 Set the low index to the first element of the array and the high index to the last element.
# 3 Set the middle index to the average of the low and high indices.
# 4 If the element at the middle index is the target element, return the middle index.
# 5 If the target element is less than the element at the middle index, set the high index to the middle index – 1.
# 6 If the target element is greater than the element at the middle index, set the low index to the middle index + 1.
# 7 Repeat steps 3-6 until the element is found or it is clear that the element is not present in the array.

import os
from modules.search import *

# Criando dados:

list_bs = gen_rand_list(10, 99)
default(list_bs)

# Iniciando programa

os.system('cls')
exit = False

while exit != True:

    print(f'a lista é: {list_bs}')
    default(list_bs)

    search = input('Digite o número a ser procurado: ')

    if search == 'exit':
        exit = True
        break

    else:
        search = int(search)
    
            
    while (index_sup - index_inf) > 1:
    
        if search == list_bs[index_mid]:
            break

        elif search > list_bs[index_mid]:
            index_inf = index_mid
            index_mid = calc_mid_index(index_inf, index_sup)
            
        elif search < list_bs[index_mid]:
            index_sup = index_mid
            index_mid = calc_mid_index(index_inf, index_sup)
            
    if search == list_bs[index_mid]:
        found(index_mid)
    
    elif search == list_bs[index_inf]:
        found(index_inf)

    elif search == list_bs[index_sup]:
        found(index_sup)

    else:
        os.system('cls')
        print('O número procurado não está na lista!')