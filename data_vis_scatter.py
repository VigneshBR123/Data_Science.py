import os
os.chdir('D:/pandas data')
import pandas as pd
import matplotlib.pyplot  as plt
cars_data=pd.read_excel('cars_details.xlsx',index_col=0)
#scatter plot
plt.scatter(cars_data['age'],cars_data['price'],c='red')
plt.title('Compersion between age and price')
plt.xlabel('age')
plt.ylabel('price')
plt.show()