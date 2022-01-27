import pandas as pd

# Abrindo csv
dados = pd.read_csv('../datasets/fifa.csv')

# Somar a aceleracao com agilidade e reação criando uma coluna nova com o total

# 1 Criando a coluna
dados['Total'] = dados['Acceleration'] + dados['Agility'] + dados['Reactions']

# Refatorando dados para apresentar somente duas colunas
dados = dados[['Name', 'Total']]

# Mostrar em ordem decrescente
dados.sort_values('Total', ascending=False)

# Exportando os dados em arquivo, cria uma coluna a mais que é o index
dados.to_csv('../exported/dados_exportados.csv')

# Exportando os dados em arquivo, sem a coluna index.
dados.to_csv('../exported/dados_exportados_sem_index.csv', index=False)

# Exportando em excel
dados.to_excel('../exported/dados_excel.xlsx', index=False)

# Exportando em txt com separador TAB \t
dados.to_csv('../exported/dados_texto.txt', index=False, sep='\t')