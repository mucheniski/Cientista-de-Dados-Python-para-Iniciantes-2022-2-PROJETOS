import pandas as pd

# Abrindo csv
dados = pd.read_csv('../datasets/fifa.csv')

print('Mostrando os nomes das colunas')
print(dados.columns)
print()

# Somar a aceleracao com agilidade e reação criando uma coluna nova com o total

# 1 Criando a coluna
dados['Total'] = dados['Acceleration'] + dados['Agility'] + dados['Reactions']

# Refatorando dados para apresentar somente duas colunas
dados = dados[['Name', 'Total']]

# Mostrar em ordem decrescente
dados.sort_values('Total', ascending = False)


print(dados)