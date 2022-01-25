import pandas as pd

# Abrindo csv
dados = pd.read_csv('../datasets/fifa.csv')

# Abrindo xlsx
dados_xlsx = pd.read_excel('../datasets/arquivo.xlsx')

# Abrindo txt
dados_txt = pd.read_csv('../datasets/fifa.csv', delimiter='\t')

# Abrindo pagina html
dados_html = pd.read_html('https://en.wikipedia.org/wiki/List_of_presidents_of_Brazil')

print(dados_html)

