import os
from search import *

os.system('cls')

# Criando o input: 

def array_find_three_func(problem_input):

    problem_output = [0,0,0]

    for i in problem_input:
        minimal = min(problem_output)
        idx = problem_output.index(minimal)
        if i > minimal:
            problem_output[idx] = i

    problem_output = set(problem_output)

    return problem_output

if __name__ == '__main__':

    problem_input = gen_rand_list(5, 99)

    print(f'\nentradas: {problem_input}\n')

    problem_output = array_find_three_func(problem_input)

    print(f'\nsaída: {problem_output}\n')

    sorted_list = sorted(problem_input, reverse=True)
    answer = set(sorted_list[:3])

    print(f'\nresposta: {answer}\n')

    # Teste

    test1 = False

    if answer == problem_output:
        test1 = True

    print(f'\nTeste 1: {test1}\n')