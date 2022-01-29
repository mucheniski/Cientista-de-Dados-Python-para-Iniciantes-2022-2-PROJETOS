import pandas as pd
import matplotlib.pyplot as plt

iceCreamDf = pd.read_csv('../datasets/icecreamsales.csv')

plt.plot(
    iceCreamDf['Temperature'],
    iceCreamDf['Sales']
)

plt.show()
