import os
os.chdir('D:/pandas data')
import pandas as pd
import matplotlib.pyplot  as plt
import numpy as np
import seaborn as sns
cars_data=pd.read_excel('cars_details.xlsx',index_col=0)
# scatter plot in seaborn
sns.set_style('darkgrid')
sns.distplot(cars_data['age'],kde=False,bins=5)
plt.xlabel('age')
plt.ylabel('Freq')
plt.title('Histogram_example')
plt.show()