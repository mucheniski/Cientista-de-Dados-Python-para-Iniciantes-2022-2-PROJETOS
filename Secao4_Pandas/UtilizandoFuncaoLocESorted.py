import pandas as pd

# Abrindo csv
dados = pd.read_csv('../datasets/fifa.csv')

# Filtrando por nacionalidade
print(dados.loc[dados['Nationality'] == 'Brazil'])

# FIltrando por idade
print(dados.loc[dados['Age'] == 35])

# Ordenando por nome em orde crescente
print(dados.sort_values('Age'))

# Ordenando por nome em orde decrescente
print(dados.sort_values('Age', ascending = False))