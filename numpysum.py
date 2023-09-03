import numpy as n
a=n.array([[1,2],[3,4]], dtype=int)
c=n.sum(a)
print(c)
c=n.sum(a,axis=1)
print(c)
c=n.sum(a,axis=0)
print(c)