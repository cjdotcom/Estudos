import pandas as pd

db = pd.read_json('data.json') #base dados gerada no ml.py com scrapy 'scrapy crawl ml -0 data.json'

title = []
for i in db['Title'][0]:
    title.append(i) #tratamento de dados na coluna de titulo

link = []
for i in db['Link'][0]:
    link.append(i) #Tratamento de dados na coluna de links

price = []
for i in range(len(db['Price'][0])):
    if db['Price'][0][i].startswith('R$'):
        price.append(db['Price'][0][i]) #Tratamento de dados na coluna de preço

df = pd.DataFrame({
    'Titulo':title,
    'Preço':price,
    'Link':link
}) #data frame com o conjunto de dados tratados.

print(df.head())