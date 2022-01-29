import pandas as pd
import numpy as np

# lendo o arquivo
titanicDf = pd.read_csv('../datasets/titanic.csv')

# Buscando apenas as colunas necessárias Colunas - Name | Age | Sex | Pclass | Survived
titanicDf = titanicDf[['Name', 'Age', 'Sex', 'Pclass', 'Survived']]

#     Filtrando somente por mulheres (female)
#     Filtrando por classe, somente a primeira classe
#     Filtrando apenas por sobrevientes
titanicDf = titanicDf.loc[
      (titanicDf['Sex'] == 'female')
    & (titanicDf['Pclass'] == 1)
    & (titanicDf['Survived'] == 1)
]

#  Mostrar os sobreviventes com SIM no lugar de 1
titanicDf.loc[
      titanicDf['Survived'] == 1,
      'Survived'
] = 'Yes'

# Ordenar os nomes em ordem alfabética
titanicDf = titanicDf.sort_values('Name', ascending=True)

# Ajustando o index pra começar com 1
titanicDf.index = np.arange(1, len(titanicDf)+1)

# Exportando o arquivo
titanicDf.to_csv('../exported/titanic_diego.csv')

print(titanicDf)