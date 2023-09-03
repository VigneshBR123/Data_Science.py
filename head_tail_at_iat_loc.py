import os
os.chdir("D:\Pandas data")
import pandas as pd
data_csv=pd.read_csv("Book1.csv")
data_csv1=data_csv.copy(deep=True)
#head
a=data_csv1.head(2)
print(a)
#tail
b=data_csv1.tail(2)
print(b)
#at
c=data_csv1.at[4,'PetalWid']
print(c)
#iat
d=data_csv1.iat[4,4]
print(d)
#
e=data_csv1.loc[0:2,'PetalWid']
print(e)