import os
from modules.gen_rand_list import *

os.system('cls')

# Criando o input: 

problem_input = gen_rand_list(5, 99)

print(f'\nentradas: {problem_input}\n')

###

problem_output = [0,0,0]

for i in problem_input:
    minimal = min(problem_output)
    idx = problem_output.index(minimal)
    if i > minimal:
        problem_output[idx] = i

problem_output = set(problem_output)

print(f'\nsaída: {problem_output}\n')

###

sorted_list = sorted(problem_input, reverse=True)
answer = set(sorted_list[:3])

print(f'\nresposta: {answer}\n')


# Teste

test1 = False

if answer == problem_output:
    test1 = True

print(f'\nTeste 1: {test1}\n')