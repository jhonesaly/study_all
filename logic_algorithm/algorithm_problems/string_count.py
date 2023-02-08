# Desafio: https://www.geeksforgeeks.org/count-uppercase-lowercase-special-character-numeric-values/
# Given a string, write a program to count the occurrence of:
# Lowercase characters, Uppercase characters, Special characters, and Numeric values.

problem_input = '*GeEkS4GeEkS*'

import string

all_low = set(string.ascii_lowercase)
all_upp = set(string.ascii_uppercase)
all_digi = set(string.digits)
all_punct = set(string.punctuation)

# count_low = 0
# count_upp = 0
# count_digi = 0
# count_punct = 0

count_low, count_upp, count_digi, count_punct = 0, 0, 0, 0

for i in problem_input:
    if i in all_low:
        count_low += 1
    elif i in all_upp:
        count_upp += 1
    elif i in all_digi:
        count_digi += 1
    elif i in all_punct:
        count_punct += 1

problem_output = [count_upp, count_low, count_digi, count_punct]
print(f'O número de caracteres maiúsculos é: {problem_output[0]}')
print(f'O número de caracteres minúsculos é: {problem_output[1]}')
print(f'O número de caracteres numéricos é: {problem_output[2]}')
print(f'O número de caracteres especiais é: {problem_output[3]}')