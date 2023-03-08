import datetime

def calculate_age(date_born_str, date_ref_str=None):

    if date_ref_str is None:
        date_ref = datetime.date.today()
    else:
        date_ref = datetime.datetime.strptime(date_ref_str, '%d/%m/%Y').date()

    date_born = datetime.datetime.strptime(date_born_str, '%d/%m/%Y').date()

    years = date_ref.year - date_born.year
    months = date_ref.month - date_born.month
    days = date_ref.day - date_born.day

    if date_born.year % 4 == 0:
        month_range =[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        day_gap = month_range[date_born.month+1] - date_born.day

    else:
        month_range =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        day_gap = month_range[date_born.month-1] - date_born.day
    
    if months < 0 or (months == 0 and days < 0):
        years -= 1
        months += 12

    if days < 0:
        months -= 1
        days = date_ref.day + day_gap

    print(date_born.month)
    
    age = f'a diferença é de {years} anos, {months} meses e {days} dias.'
    return print(age)