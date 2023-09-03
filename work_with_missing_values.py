import os
os.chdir("D:/pandas data")
import pandas as pd
cars_data=pd.read_excel("nan_values.xlsx",index_col=0)
cars_data1=cars_data.copy(deep=True)
#describe()
print(cars_data1.describe())
#fill the nan values in numerical
#age
print(cars_data1['age'].mean())
cars_data1['age'].fillna(cars_data1['age'].mean(),inplace=True)
#km
print(cars_data1['km'].median())
cars_data1['km'].fillna(cars_data1['km'].median(),inplace=True)
#to check null values
print(cars_data1.isnull().sum())
#fill the categorical value
print(cars_data1['fuel type'].value_counts())
#frequent data
print(cars_data1['fuel type'].value_counts().index[0])
#fuel type
cars_data1['fuel type'].fillna(cars_data1['fuel type'].value_counts().index[0],inplace=True)
print(cars_data1.isna().sum())
#using lampda function
cars_data2=cars_data.copy(deep=True)
cars_data2=cars_data2.apply(lambda x:x.fillna(x.mean()) if x.dtypes=='float' else x.fillna(x.mode().index[0]))
print(cars_data2)