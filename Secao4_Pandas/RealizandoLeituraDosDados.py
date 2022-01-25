import pandas as pd

# Abrindo csv
dados = pd.read_csv('../datasets/fifa.csv')

print('Mostrando somente as primeiras 5 entradas')
print(dados.head())
print()

print('Mostrando somente as ultimas 5 entradas')
print(dados.tail())
print()

print('Mostrando somente as primeiras 2 entradas')
print(dados.head(2))
print()

print('Mostrando os nomes das colunas')
print(dados.columns)
print()

print('Mostrando as linhas por número')
print(dados.index)
print()

print('Mostrando somente dados de uma coluna específica')
print(dados['Name'])
print()

print('Mostrando somente dados de colunas específicas')
print(dados[['Name', 'Nationality', 'Wage']])
print()

print('Localizar uma linha específica')
print(dados.iloc[1])
print()

print('Localizar um range de linhas')
print(dados.iloc[1:4])
print()

print('Localizar uma linha por index [linha, coluna]')
print(dados.iloc[2,2])
print()