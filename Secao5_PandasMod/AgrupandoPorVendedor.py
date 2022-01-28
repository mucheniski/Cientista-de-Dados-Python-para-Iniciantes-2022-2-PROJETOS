import pandas as pd

# df = DataFrame
df = pd.read_csv('../datasets/house.csv')

# Agrupa por vendedor e tira uma média de cada um
# print(df.groupby(['SellerG']).mean())

# Soma o total de vendas por vendedor e ordena por preço, fazendo um top 10
print(
      df.groupby(['SellerG'])
        .sum()
        .sort_values('Price', ascending=False)
        .head(10)
)


# Contando a quantidade de quartos
print(
      df.groupby(['SellerG'])
        .count()
        .sort_values('Rooms', ascending=False)
)
