import datetime

def day_week(day_input_str):
    day_input_date = datetime.datetime.strptime(day_input_str, '%d/%m/%Y').date()
    
    day_date_ref = datetime.date(2023,3,18)
    day_week_int_ref = 7

    diff_days = (day_input_date - day_date_ref).days
    diff_day_week = diff_days % 7
    day_of_week = diff_day_week
    return day_of_week

if __name__ == '__main__':
    problem_input_1 = '25/3/2023'
    problem_output = day_week(problem_input_1)
    print(problem_output)