import pandas as pd

# lendo o arquivo
titanicDf = pd.read_csv('../datasets/titanic.csv')

# Buscando apenas as colunas necessárias Colunas - Name | Age | Sex | Pclass | Survived
titanicDf = titanicDf[['Name', 'Age', 'Sex', 'Pclass', 'Survived']]
print(titanicDf)