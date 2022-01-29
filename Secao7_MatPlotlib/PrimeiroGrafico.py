import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importando o csv para um dataframe com pandas
gasdf = pd.read_csv('../datasets/gas_prices.csv')
# print(gasdf)

# Criando um gráfico de linhas comparando preços entre 3 países eixos x, y

# Adicionando título
plt.title("Valores de combustível em US$")

# Adicionando valores (eixo X, eixo Y)
plt.plot(gasdf['Year'], gasdf['Australia'], label='Australia')
plt.plot(gasdf['Year'], gasdf['Italy'], label='Italy')
plt.plot(gasdf['Year'], gasdf['USA'], label='USA')
plt.plot(gasdf['Year'], gasdf['Japan'], label='Japan')

# Formatando o valor dos anos no eixo X
# [::2] do início ao fim apresentando de 2 em 2 anos
plt.xticks(gasdf['Year'][::2])

# Adicoinando a legenda e apresentando o gráfico
plt.legend()
plt.show()