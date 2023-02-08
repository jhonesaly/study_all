


#tempo_meta_anos = int(input('Digite o tempo disponível [anos]: '))
#lucro_mensal = int(input('Digite meta de valor mensal [R$]: '))
#taxa_selic = float(input('Digite o valor da taxa selic [%]: '))

#Tratar dados
#...
#

tempo_meta_anos = 30
taxa_selic = 0.1375
lucro_mensal = 30000

selic_mensal_raw = ((1+taxa_selic)**(1/12))-1
selic_mensal = round(selic_mensal_raw, 4)

meta_ativos = lucro_mensal/selic_mensal

tempo_meta_meses = tempo_meta_anos*12

aporte_mensal_raw = (meta_ativos*selic_mensal)/(((1+selic_mensal)**tempo_meta_meses)-1)
aporte_mensal = round(aporte_mensal_raw, 2)

print(aporte_mensal)

montante = 130000
lista_anual = {}
#Imposto
#Inflação


for t in range(tempo_meta_meses):
    rendimento = montante*selic_mensal
    montante = montante + aporte_mensal + rendimento
    print(f'no mês {t} rendeu {rendimento:.2f} e  o montante total é {montante:.2f}')

    if t%12 == 0:
        lista_anual[t/12]=round(rendimento,2)
        

for i in lista_anual:
    print(int(i), lista_anual[i])