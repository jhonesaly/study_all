def reversal(list, search):
    list_reversal = [0 for i in range(search)]

    for i in range(search):
        aux_1 = list.pop(-1)
        aux_2 = search - i - 1
        list_reversal[aux_2] = aux_1

    list_reversal.extend(list)

    return list_reversal

###
if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    problem_input2 = 2
    problem_output = reversal(list, problem_input2)
    print(f'\nsaída: {problem_output}\n')