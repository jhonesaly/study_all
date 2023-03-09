# Given an array arr[] consisting of N strings 
# and an array Query[] consisting of Q queries. 
# Each string in arrays arr[] and Query[] is of the form D/M/Y where D, M and Y denotes the date, month and year. 
# For each query, the task is to print the next closest date from the given array arr[]. 
# If no such date exists, print “-1”.

import datetime

def find_future(dates_ref_str, dates_search_str):
    
    dates_ref_list = []
    for date_str in dates_ref_str:
        dates_ref_list.append(datetime.datetime.strptime(date_str, '%d/%m/%Y').date())
    
    dates_search_list = []
    for date_str in dates_search_str:
        dates_search_list.append(datetime.datetime.strptime(date_str, '%d/%m/%Y').date())

    answer = []
    for date_search in dates_search_list:
        diff_list = []
        for date_ref in dates_ref_list:
            diff_date = abs((date_ref - date_search).days)
            diff_list.append(diff_date)

        min_diff = min(diff_list)
        min_index = diff_list.index(min_diff)
        answer.append(dates_ref_list[min_index])
    
    return answer

if __name__ == '__main__':
    problem_input_1 = ['22/4/1233', '1/3/0633', '23/5/5665', '4/12/2330'] 
    problem_input_2 = ['23/3/4345', '25/5/1244']

    problem_output = find_future(problem_input_1, problem_input_2)
    print(problem_output)


