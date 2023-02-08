# Cálculo de rendimentos

def calc_lucro (montante, type, index, year):
    print('---------------------')
    lucro = round(montante*index, 2)
    print(f'lucro {type} {year}: {lucro}')
    new_montante = montante + lucro
    print(f'novo montante: {new_montante}')
    return new_montante

montante = 60000

# Rendimento poupança
index_poupanca_2021 = 7.9 / 100
index_poupanca_2022 = 7.89 /100

# Rendimento IFIX (https://omentorfinanceiro.com.br/investimentos/ifix-2023-mensal-e-acumulado/)
index_fundos_imob_2021 = -2.28 / 100
index_fundos_imob_2022 = 2.22 / 100

montante2022_p = calc_lucro(    montante,         'poupança',             index_poupanca_2021,    2021)
montante2023_p = calc_lucro(    montante2022_p,   'poupança',             index_poupanca_2022,    2022)
montante2022_fim = calc_lucro(  montante,         'fundo imobiliários',   index_fundos_imob_2021, 2021)
montante2023_fim = calc_lucro(  montante2022_fim, 'fundo imobiliários',   index_fundos_imob_2022, 2022)