import os
from modules.gen_rand_list import *

os.system('cls')

# Criando o input: 

#problem_input1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
problem_input2 = 5
problem_input1 = gen_rand_list(10, 99)
#problem_input2 = gen_rand_list(1,5).append()


print(f'\nentradas: {problem_input1} , {problem_input2}\n')

###

problem_output = [0 for i in range(problem_input2)]

for i in range(problem_input2):
    aux_1 = problem_input1.pop(-1)
    aux_2 = problem_input2 - i - 1
    problem_output[aux_2] = aux_1

problem_output.extend(problem_input1)
print(f'\nsaída: {problem_output}\n')

###

# answer = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
# print(f'\nresposta: {answer}\n')

# Teste

# test1 = False

# if answer == problem_output:
#     test1 = True

# print(f'\nTeste 1: {test1}\n')