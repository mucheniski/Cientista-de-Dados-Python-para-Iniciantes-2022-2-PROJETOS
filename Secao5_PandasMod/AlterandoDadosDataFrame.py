import pandas as pd
import re

# df = DataFrame
df = pd.read_csv('../datasets/house.csv')

# Buscando um vendedor
seller = df.loc[
    df['SellerG'] == 'Barry'
]

# Alterando o nome do vendedor no df
df.loc[
    df['SellerG'] == 'Barry',
    'SellerG'
] = 'Barry Alan'


# df.loc[
#     df['SellerG'] == 'Barry', Toda vez que eu encontrar Barry
#     'SellerG' Na coluna SellerG
# ] = 'Barry Alan' Eu quero trocar para Barry Alan

# print(df['SellerG'])

# Trocando o valor da coluna Method para o Barry Alan apenas
df.loc[
    df['SellerG'] == 'Barry Alan',
    'Method'
] = 'Pending'

# print(df['Method'])

# Trocando o valor da coluna Method e de Type para o Barry Alan apenas
df.loc[
    df['SellerG'] == 'Barry Alan',
    ['Method', 'Type']
] = 'Pending'

print(df[['Method', 'Type', 'SellerG']])
