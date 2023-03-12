# You are given a time T in 24-hour format (hh:mm) and a positive integer K, 
# you have to tell the time after K minutes in 24-hour time.
import datetime

def sum_minute (T:str, K:int|str) -> str:
    date_hour = datetime.datetime.strptime(T, "%H:%M")
    if isinstance(K, str):
        try:
            K = int(K)
        except ValueError:
            raise ValueError("Invalid value for second argument")

    new_T = date_hour + datetime.timedelta(minutes=K)
    new_T_str = new_T.strftime("%H:%M")

    return new_T_str

if __name__ == "__main__":
    test = sum_minute('20:39', 534)
    print(test)