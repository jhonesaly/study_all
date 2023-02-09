import random
import datetime
import os

start = datetime.datetime(1, 1, 1)
end = datetime.datetime(9999, 12, 31)

def gen_rand_datetime(n, start=start, end=end):
    date_list = []
    for i in range(n):
        date = start + datetime.timedelta(
            seconds=random.randint(0, int((end - start).total_seconds())))
        date_list.append(date.strftime("%d/%m/%Y"))
    return date_list

if __name__ == "__main__":
    os.system('cls')
    n = 4
    date_list = gen_rand_datetime(4)
    print(date_list)
