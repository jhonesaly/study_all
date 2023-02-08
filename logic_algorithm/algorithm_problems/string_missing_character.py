# Desafio: https://www.geeksforgeeks.org/missing-characters-make-string-pangram/
# Pangram is a sentence containing every letter in the English alphabet. 
# Given a string, find all characters that are missing from the string, i.e., 
# the characters that can make the string a Pangram. 
# We need to print output in alphabetic order.

import string
import random

# char_all = set(string.ascii_letters)
# digi_all = set(string.digits)
# punct_all = set(string.punctuation)
# str_all = char_all | digi_all | punct_all
# print(str_all)

#size = 10
#caracteres = string.ascii_letters + string.digits + string.punctuation
#string_aleatoria = "".join(random.choices(caracteres, k=size))
# print(string_aleatoria)

problem_input = 'The quick brown fox jumps'

char_list = problem_input.lower()
char_list = [str for str in char_list]
char_list = set(char_list)

char_all = set(string.ascii_lowercase)

char_missing = char_all.difference(char_list)
char_missing = list(char_missing)
char_missing.sort()
char_missing = "".join(char_missing)

problem_output = char_missing
print(problem_output)