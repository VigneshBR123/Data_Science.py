import os
os.chdir('D:/pandas data')
import pandas as pd
cars_data=pd.read_excel('cars_details.xlsx',index_col=0)
cars_data1=cars_data.copy(deep=True)
#multiple i/d and o/p
def c_convert(val1,val2):
    age_converted=val1/12
    performed=val2/val1
    return age_converted,performed
cars_data1['age_converted_at'],cars_data1['performed']=c_convert(cars_data1['age'],cars_data1['km'])
print(cars_data1)
#frequency tables
cars_data2=pd.crosstab(index=cars_data1['age'],columns='count')
print(cars_data2)
# two way tables
cars_data2=pd.crosstab(index=cars_data1['gear'],columns=cars_data1['fuel type'])
print(cars_data2)
#joint probability
cars_data2=pd.crosstab(index=cars_data1['gear'],columns=cars_data1['fuel type'],normalize=True)
print(cars_data2)
#marginal probability
cars_data2=pd.crosstab(index=cars_data1['gear'],columns=cars_data1['fuel type'],normalize=True,margins=True)
print(cars_data2)
#condition probability
cars_data2=pd.crosstab(index=cars_data1['gear'],columns=cars_data1['fuel type'],normalize='columns',margins=True)
print(cars_data2)
#correlation
numerical_data=cars_data1.select_dtypes(exclude=['object'])
print(numerical_data)
print(numerical_data.shape)
corr_matrix=numerical_data.corr()
print(corr_matrix)