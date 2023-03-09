# Given an array arr[] consisting of N strings 
# and an array Query[] consisting of Q queries. 
# Each string in arrays arr[] and Query[] is of the form D/M/Y where D, M and Y denotes the date, month and year. 
# For each query, the task is to print the next closest date from the given array arr[]. 
# If no such date exists, print “-1”.

import datetime

def find_future(dates_ref_str, search_str):
    
    dates_ref_list = []
    for date_str in dates_ref_str:
        dates_ref_list.append(datetime.datetime.strptime(date_str, '%d/%m/%Y').date())
    
    date_search = datetime.datetime.strptime(search_str, '%d/%m/%Y').date()
    
    diff_list = []
    for date_ref in dates_ref_list:
        diff_date = abs((date_ref - date_search).days)
        diff_list.append(diff_date)

    min_diff = min(diff_list)
    min_index = diff_list.index(min_diff)
    answer = dates_ref_list[min_index]
    print(answer)

    answer = -1

    return answer


problem_input_1 = ['22/4/1233', '1/3/0633', '23/5/5665', '4/12/2330'] 
problem_input_2 = '23/3/4345'

find_future(problem_input_1, problem_input_2)

# problem_answer = ['23/5/56645', '4/12/233']




# n = int(input("Enter the number of random dates to generate: "))

# if ...:

# else:
#     problem_output = -1


