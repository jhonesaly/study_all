import random

## Criando lista de dados

def gen_rand_list(list_range, lim_sup, lim_inf=0):
    # modo alternativo: list = random.sample(range(list_range), list_size)    
    
    list = []
    for num in range(list_range):
        num = random.randint(lim_inf, lim_sup)
        list.append(num)
    return list