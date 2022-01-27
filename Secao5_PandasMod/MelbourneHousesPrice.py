import pandas as pd
import re

# df = DataFrame
df = pd.read_csv('../datasets/house.csv')

# print(df)

# Apenas casas com 3 quartos que estejam abaixo do valor 300000
exemplo1 = df.loc[
                  (df['Type'] == 'h')
                & (df['Rooms'] == 3)
                & (df['Price'] <= 300000)
            ]

# print(exemplo1)

# Localizar apenas um endereço específico
exemplo2 = df.loc[
    df['Address'].str.contains('Turner')
]

# print(exemplo2)

# Localizar apenas um endereço específico que contenha uma palavra ou outra
# ou é representado pelo pipe |
# flags=re.I significa que é uma regular expression e o ,I é para ignorar maíusculas e minúsculas e filtrar do mesmo jeito
exemplo3 = df.loc[
    df['Address'].str.contains('Turner St | Turner Rd', flags=re.I)
]

# print(exemplo3)

# Localizar casa em uma rua específica com um determinado preço
# regular expressions and conditions
# ^59 significa inicie com 59
exemplo4 = df.loc[
      (df['Address'].str.contains('^59', flags=re.I))
    & (df['Price'] <= 500000)
]
print(exemplo4)
