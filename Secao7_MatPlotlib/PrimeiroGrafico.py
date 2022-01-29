import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importando o csv para um dataframe com pandas
gasdf = pd.read_csv('../datasets/gas_prices.csv')
# print(gasdf)

# Criando um gráfico de linhas comparando preços entre 3 países eixos x, y

# Adicionando título
plt.title("Gas Price in US$")

# Adicionando valores (eixo X, eixo Y)
plt.plot(
    gasdf['Year'], # Eixo X
    gasdf['Australia'], # Eixo Y
    'r.-', # cor e tipo da linha, vermelha pontilhada e com traços entre os pontos
    label='Australia'
)

plt.plot(
    gasdf['Year'],
    gasdf['Italy'],
    'y.-',
    label='Italy'
)

plt.plot(
    gasdf['Year'],
    gasdf['USA'],
    'b.-',
    label='USA'
)

plt.plot(
    gasdf['Year'],
    gasdf['Japan'],
    'g.-',
    label='Japan'
)

# Formatando o valor dos anos no eixo X
# [::2] do início ao fim apresentando de 2 em 2 anos
plt.xticks(gasdf['Year'][::2])

# Adicionando título para o eixo X
plt.xlabel('Years')

# Adicionando título para o eixo Y
plt.ylabel('US$')

# Adicoinando a legenda e apresentando o gráfico
plt.legend()
plt.show()