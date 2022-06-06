# -*- coding: utf-8 -*-
#Associação
#Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

#Tabela pandas
store_data = pd.read_excel('remedios.xlsx', header=None)
print(store_data)
records = []

coluna = store_data.shape[1]
coluna = coluna + 1

for i in store_data.itertuples():
    incluirlista = []
    incluirlista.append(str(i[1]))
    for j in range(2,coluna):
        if (str(i[j])!='nan'):
            incluirlista.append(str(i[j]))    
    records.append(incluirlista)

#Fim tabela pandas
print()
for i in records:
    print(i)

association_rules = apriori(records, min_support = 0.1, min_confidence = 0.5, min_lift = 1.3)
association_results = list(association_rules)

contador = 0
for item in association_results:
    print()
    #print(item)
    suporte = item[1]
    for x in item[2]:
        origem = ''
        destino = ''

        #ORIGEM
    for i in x[0]:
        if (origem == ''):
            origem = i
        else:
            origem = origem + ', ' + i
        
        #DESTINO
    for i in x[1]:
        if (destino == ''):
            destino = i
        else:
            destino = destino + ', ' + i

    if (origem != '' and destino != ''):
        print(f'Clientes que compraram: {origem} --> {destino}')
        contador += 1
        print(f"Support: {suporte:.2f}")
        print(f'Confidence: {x[2]:.2f}')
        print(f'Lift: {x[3]:.2f}')
        print('='*47)
print()
print(f'RESULTADOS: {contador}')
