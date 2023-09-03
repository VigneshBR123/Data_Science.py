import os
os.chdir("D:\Pandas data")
import pandas as pd
data_csv=pd.read_csv("Book1.csv")
#check dtypes
a=data_csv.dtypes
print(a)
#count of unique datatypes
b=data_csv.dtypes.value_counts()
print(b)
#ignoring data type
c=data_csv.select_dtypes(exclude=['object'])
print(c)
#info
d=data_csv.info()
print(d)
#unique elements of column
import numpy as np
e=np.unique(data_csv['PetalLen'])
print(e)
#replace special character into nan
data_csv=pd.read_csv("Book1.csv",na_values=['??','###'])
print(data_csv)
print(data_csv.info())
#covert dtypes
data_csv['PetalWid']=data_csv['PetalWid'].astype('int64')
print(data_csv.dtypes)
#object vs category
print(data_csv['species'].nbytes)
data_csv['species']=data_csv['species'].astype('category')
print(data_csv['species'].nbytes)
#to find null values
print(data_csv.isnull().sum())