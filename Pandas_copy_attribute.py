import os
os.chdir("D:\Pandas data")
import pandas as pd
data_csv=pd.read_csv("Book1.csv")
data_csv1=data_csv.copy(deep=True)
#print rows
a=data_csv1.Speallength
print(a)
#print columns
b=data_csv1.columns
print(b)
#print rows * columns
c=data_csv.size
print(c)
#print row & column
d=data_csv1.shape
print(d)
#memory usuage
e=data_csv1.memory_usage()
print(e)
#no.of dimension
f=data_csv1.ndim
print(f)