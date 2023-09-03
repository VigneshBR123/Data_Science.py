import numpy as sa
a=sa.arange(24)
print(a)
print(a.ndim)
print(a.shape)
a=a.reshape(3,-1)
print(a)
a=a.reshape(6,4,1)
print(a)