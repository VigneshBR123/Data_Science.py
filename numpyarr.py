import numpy as gh
lst=[1,2,3,4,5,6]
a=gh.array(lst, dtype=int)
print(type(a))
print(a)
print(len(a))
print(a.ndim)
print(a.shape)
a=a.reshape(2,-1)
print(a)