import datetime

def day_week(day_input_str):
    day_input_date = datetime.datetime.strptime(day_input_str, '%d/%m/%Y').date()
    
    day_date_ref = datetime.date(2023,3,18)
    day_week_int_ref = 7

    diff_days = (day_input_date - day_date_ref).days

    day_of_week = diff_days
    return day_of_week

if __name__ == '__main__':
    problem_input_1 = '20/4/2023'
    problem_output = day_week(problem_input_1)
    print(problem_output)