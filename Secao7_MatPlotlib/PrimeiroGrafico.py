import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importando o csv para um dataframe com pandas
gasdf = pd.read_csv('../datasets/gas_prices.csv')
print(gasdf)

# Criando um gráfico de linhas comparando preços entre 3 países eixos x, y
plt.plot(gasdf['Year'], gasdf['Australia'])
plt.plot(gasdf['Year'], gasdf['Italy'])
plt.plot(gasdf['Year'], gasdf['USA'])
plt.show()