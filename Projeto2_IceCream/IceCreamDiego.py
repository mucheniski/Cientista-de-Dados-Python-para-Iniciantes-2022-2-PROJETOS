import pandas as pd
import matplotlib.pyplot as plt

iceCreamDf = pd.read_csv('../datasets/icecreamsales.csv')
iceCreamDf = iceCreamDf.sort_values('Temperature', ascending=False)

# Convertendo fahrenheit em celsius e salvando no dataframe
celsius = (iceCreamDf['Temperature'] - 32) * 5/9
iceCreamDf['Temperature'] = celsius

plt.plot(
    iceCreamDf['Temperature'],
    iceCreamDf['Sales'],
    'r.--',
    label='US$'
)

plt.title('Ice Cream Truck')
plt.xlabel('Temperature')
plt.ylabel('Sales (US$)')

plt.legend()

plt.savefig('../grafics/iceCreamDiego.pdf')

plt.show()
