import os
os.chdir('D:/pandas data')
import pandas as pd
import matplotlib.pyplot  as plt
cars_data=pd.read_excel('cars_details.xlsx',index_col=0)
#Histogram
plt.hist(cars_data['km'],color='green', edgecolor='black', bins=5)
plt.title('Histogram of Kilometer')
plt.xlabel('km')
plt.ylabel('Freq')
plt.show()