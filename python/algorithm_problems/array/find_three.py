import os

os.system('cls')

# Criando o input: 

def find_three(list):

    max_three = [0,0,0]

    for i in list:
        minimal = min(max_three)
        idx = max_three.index(minimal)
        if i > minimal:
            max_three[idx] = i

    max_three = set(max_three)

    return max_three

if __name__ == '__main__':

    problem_input = [3, 31, 63, 74, 15]
    problem_output = find_three(problem_input)

    print(problem_output)