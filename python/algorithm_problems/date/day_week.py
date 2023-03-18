import datetime

def day_week(input_date_str):
    mid = datetime.datetime.strptime(input_date_str, '%d/%m/%Y').date()
    print(mid)
    day_of_week = []
    return day_of_week

if __name__ == '__main__':
    problem_input_1 = '18/3/2023'
    problem_output = day_week(problem_input_1)
    print(problem_output)