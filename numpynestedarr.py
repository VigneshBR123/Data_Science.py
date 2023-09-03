import numpy as bg
lst=[1,2,3,4,5,6]
lst1=[2,3,4,5,6,7]
lst2=[3,4,5,6,7,8]
lst3=[4,5,6,7,8,9]
a=bg.array([lst,lst1,lst2,lst3])
print(a)
print(a.shape)
a=a.reshape(1,-1)
print(a)