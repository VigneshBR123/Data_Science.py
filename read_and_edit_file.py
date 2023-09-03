import os
os.chdir("D:\Pandas data")
import pandas as pd
data_csv=pd.read_csv("Book1.csv",index_col=1,na_values=["??","###"])
print(data_csv)