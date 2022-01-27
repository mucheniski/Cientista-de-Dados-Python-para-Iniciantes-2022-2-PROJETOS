import pandas as pd

# df = DataFrame
df = pd.read_csv('../datasets/house.csv')

# print(df)

# Apenas casas com 3 quartos que estejam abaixo do valor 300000
exemplo1 = df.loc[
                  (df['Type'] == 'h')
                & (df['Rooms'] == 3)
                & (df['Price'] <= 300000)
            ]

print(exemplo1)