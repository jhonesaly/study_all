# Desafio: https://www.geeksforgeeks.org/bubble-sort/
# Bubble Sort is the simplest sorting algorithm that works by repeatedly # swapping the adjacent elements if they 
# are in the wrong order. This algorithm # is not suitable for large data sets as its average and worst-case time 
# complexity is quite high.

import os
from modules.search import *

os.system('cls')

# problem_input = [8, 5, 4, 2, 1]

problem_input = gen_rand_list(20, 99)

# Solution 1:

# problem_input.sort()
# print(problem_input)

# Solution 2 (algorithm):

list_raw = problem_input

for x in range(len(list_raw)):    
    print(f'*****\nentrando no ciclo {x+1}')
    for i in range(len(list_raw)-1):
        print(f'---\nindex: {i}')
        print(f'i: {list_raw[i]}')
        print(f'i+1: {list_raw[i+1]}')
        if list_raw[i] > list_raw[i+1]:
            print('maior que o sucessor')
            num_l = list_raw[i]
            num_r = list_raw[i+1]
            list_raw[i] = num_r
            list_raw[i+1] = num_l
        else:
            print('não é maior que o sucessor')
    
    print(f'fim do ciclo {x+1}')

print(list_raw)

# problem_answer = [1, 2, 4, 5, 8] 
