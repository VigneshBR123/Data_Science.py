import os
os.chdir('D:/pandas data')
import pandas as pd
import matplotlib.pyplot  as plt
import numpy as np
import seaborn as sns
cars_data=pd.read_excel('cars_details.xlsx',index_col=0)
# scatter plot in seaborn
sns.set_style('darkgrid')
sns.lmplot(x='age',y='price',data=cars_data,fit_reg=False,hue="fuel type",legend=True,palette='pastel')
plt.xlabel('age')
plt.ylabel('price')
plt.title('Age vs Price')
plt.show()