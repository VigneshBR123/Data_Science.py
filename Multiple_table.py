import os
os.chdir('D:/pandas data')
import pandas as pd
import matplotlib.pyplot  as plt
import numpy as np
import seaborn as sns
cars_data=pd.read_excel('cars_details.xlsx',index_col=0)
# mulptiple table plot in seaborn
f,(ax_box,ax_hist)=plt.subplots(2,gridspec_kw={"height_ratios":(.15,.85)})
sns.boxplot(x='price',data=cars_data,ax=ax_box)
sns.distplot(cars_data['price'],ax=ax_hist,kde=False)
plt.xlabel('Freq')
plt.ylabel('Price')
plt.title('Boxplot And Whisker_example')
plt.show()