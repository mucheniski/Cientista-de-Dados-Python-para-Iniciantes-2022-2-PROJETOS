import pandas as pd
import matplotlib.pyplot as plt

# Importando o csv para um dataframe com pandas
gasdf = pd.read_csv('../datasets/gas_prices.csv')
# print(gasdf)

# Criando um gráfico de linhas comparando preços entre 3 países eixos x, y

# Adicionando título
plt.title("Gas Price in US$")

# Populando os valores com for em uma lista, basta adicionar nesta lista que o gráfico é populado
list_country = ['Australia', 'USA', 'Italy', 'Germany']

for country in gasdf:
    if country in list_country:
        plt.plot(
            gasdf['Year'],
            gasdf[country],
            label=country,
            marker='.'
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