import os
os.chdir('D:/pandas data')
import pandas as pd
import matplotlib.pyplot  as plt
import numpy as np
cars_data=pd.read_excel('cars_details.xlsx',index_col=0)
#bar plot
counts=[917,120,12]
fueltype=['petrol','disel','battery']
index=np.arange(len(fueltype))
plt.bar(index,counts,color=['black','blue','gray'])
plt.title('Bar plot example')
plt.xlabel('fuel type')
plt.ylabel('counts')
plt.xticks(index,fueltype,rotation=120)
plt.show()