# Algoritmo: https://www.geeksforgeeks.org/counting-sort/

# Counting sort is a sorting technique based on keys between a specific range. 
# It works by counting the number of objects having distinct key values (a kind of hashing). 
# Then do some arithmetic operations to calculate the position of each object in the output sequence. 


import os
from modules.gen_rand_list import *

os.system('cls')

# Criando o input: 

problem_input = gen_rand_list(10, 99)

print(f'\n entradas: {problem_input}\n')

# Criando chave:

key_index = list(range(min(problem_input),max(problem_input)+1))
key_zeros = list(0 for i in range(len(key_index)))

for i1 in range(len(problem_input)):
    for i2 in range(len(key_index)):
        if key_index[i2] == problem_input[i1]:
            key_zeros[i2] += 1

print(f'\n chaves: {key_index}\n')
print(f'\n fechadura: {key_zeros}\n')

problem_output = []

for i in range(len(key_zeros)):
    while key_zeros[i] != 0:
        problem_output.append(key_index[i])
        key_zeros[i] -= 1
            

print(f'\n saídas: {problem_output}\n')

answer = sorted(problem_input)

print(f'\n resposta: {answer}\n')

# print(answer)

# Teste

test1 = False

if answer == problem_output:
    test1 = True

print(f'Teste 1: {test1}')