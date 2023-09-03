import os
os.chdir("D:/pandas data")
import pandas as pd
data_cars=pd.read_excel("cars_details.xlsx",index_col=0)
print(data_cars)
#to insert new col
data_cars.insert(6,"price_class",0)
for i in range(1,len(data_cars['price'])+1,1):
    if data_cars['price'][i]<=9000:
        data_cars['price_class'][i]='low'
    elif data_cars['price'][i]>=12000:
        data_cars['price_class'][i]='high'
    else:
        data_cars["price_class"][i]='medium'
print(data_cars)
#count no.of data in particular category
print(data_cars['price_class'].value_counts())
#using function
data_cars.insert(7,'age_converted',0)
def c_convert(val):
    age_converted=val/12
    return age_converted
data_cars['age_converted']=c_convert(data_cars['age'])
data_cars['age_converted']=round(data_cars['age_converted'],1)
print(data_cars)
#multiple i/p and o/p