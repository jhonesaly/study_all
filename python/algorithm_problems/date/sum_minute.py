# You are given a time T in 24-hour format (hh:mm) and a positive integer K, 
# you have to tell the time after K minutes in 24-hour time.
import datetime

def sum_minute (init_hour_str:str, add_minutes:int|str) -> str:
    
    init_date_hour = datetime.datetime.strptime(init_hour_str, "%H:%M")
    
    if isinstance(add_minutes, str):
        try:
            add_minutes = int(add_minutes)
        except ValueError:
            raise ValueError("Invalid value for second argument")

    new_date_hour = init_date_hour + datetime.timedelta(minutes=add_minutes)
    new_date_hour_str = new_date_hour.strftime("%H:%M")

    return new_date_hour_str

if __name__ == "__main__":
    test = sum_minute('20:39', 534)
    print(test)