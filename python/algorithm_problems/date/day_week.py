import datetime

def day_week(day_str):
    day_date = datetime.datetime.strptime(day_str, '%d/%m/%Y').date()
    
    day_ref = datetime.date(2023,3,18)
    day_week_ref = 7

    day_of_week = day_ref
    return day_of_week

if __name__ == '__main__':
    problem_input_1 = '18/3/2023'
    problem_output = day_week(problem_input_1)
    print(problem_output)