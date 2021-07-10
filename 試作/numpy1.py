import numpy as np

b=np.array([[2, 5], [1, 3]])
c=np.array([[2,4],[3,2]])

e=np.multiply(b,c) #行列の積
print(e)
f=b@c
print(f)
d=np.linalg.inv(b) #逆行列
print(d)