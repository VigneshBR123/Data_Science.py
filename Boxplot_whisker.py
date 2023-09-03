import os
os.chdir('D:/pandas data')
import pandas as pd
import matplotlib.pyplot  as plt
import numpy as np
import seaborn as sns
cars_data=pd.read_excel('cars_details.xlsx',index_col=0)
# scatter plot in seaborn
sns.set_style('darkgrid')
sns.boxplot(y='price',x='fuel type',data=cars_data,hue='gear')
plt.xlabel('Freq')
plt.ylabel('Price')
plt.title('Boxplot And Whisker_example')
plt.show()