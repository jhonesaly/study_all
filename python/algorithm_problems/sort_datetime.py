import os

def sort_datetime(raw_date):
    sorted_date = []
    sep_date = []
    for date in raw_date:
        sep_date.append(date.split('/'))
    
    print(sep_date)
    print(sorted_date)
    




if __name__ == '__main__':
    os.system('cls')
    raw_date = ['22/4/1233', '1/3/633', '23/5/56645', '4/12/233']
    print(raw_date)
    sort_datetime(raw_date)
    
    
    

