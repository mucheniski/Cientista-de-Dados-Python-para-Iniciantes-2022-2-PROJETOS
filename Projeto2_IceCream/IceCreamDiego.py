import pandas as pd
import matplotlib.pyplot as plt

iceCreamDf = pd.read_csv('../datasets/icecreamsales.csv')

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
