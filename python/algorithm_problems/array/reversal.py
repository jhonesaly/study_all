import os
from search import *

os.system('cls')

###
def reversal(list, search):
    problem_output = [0 for i in range(search)]

    for i in range(search):
        aux_1 = problem_input1.pop(-1)
        aux_2 = search - i - 1
        problem_output[aux_2] = aux_1

    problem_output.extend(problem_input1)
    print(f'\nsaída: {problem_output}\n')
    return problem_output

###
if __name__ == '__main__':
    problem_input1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    problem_input2 = 5


# answer = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
# print(f'\nresposta: {answer}\n')

# Teste

# test1 = False

# if answer == problem_output:
#     test1 = True

# print(f'\nTeste 1: {test1}\n')