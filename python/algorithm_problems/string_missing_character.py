# Desafio: https://www.geeksforgeeks.org/missing-characters-make-string-pangram/
# Pangram is a sentence containing every letter in the English alphabet. 
# Given a string, find all characters that are missing from the string, i.e., 
# the characters that can make the string a Pangram. 
# We need to print output in alphabetic order.

import string

# char_all = set(string.ascii_letters)
# digi_all = set(string.digits)
# punct_all = set(string.punctuation)
# str_all = char_all | digi_all | punct_all
# print(str_all)

#size = 10
#caracteres = string.ascii_letters + string.digits + string.punctuation
#string_aleatoria = "".join(random.choices(caracteres, k=size))
# print(string_aleatoria)



def char_missing(text):

    char_input = text.lower()
    char_input = [str for str in char_input]
    char_input = set(char_input)

    char_all = set(string.ascii_lowercase)

    char_missing = char_all.difference(char_input)
    char_missing = list(char_missing)
    char_missing.sort()
    char_missing = "".join(char_missing)
        
    return char_missing

problem_input = 'The quick brown fox jumps'
problem_output = char_missing(problem_input)