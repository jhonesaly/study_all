import random
import datetime

start = datetime.datetime(0000, 1, 1)
end = datetime.datetime(9999, 12, 31)

def gen_rand_datetime(n, start=start, end=end):
    date_lst = []
    for i in range(n):
        date = start + datetime.timedelta(
            seconds=random.randint(0, int((end - start).total_seconds())))
        date_lst.append(date)
    return date_lst