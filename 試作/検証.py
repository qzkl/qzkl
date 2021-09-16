import numpy as np
import math
import matplotlib.pyplot as plt

x=[]
y_np=[]
y_math=[]


def tanh_np(x):
    return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))

def tanh_math(x):
    return (math.exp(x)-math.exp(-x))/(math.exp(x)+math.exp(-x))

for i in np.arange(-2.0, 2.0, 0.1):
    x.append(i)
    y_np.append(tanh_np(i))
    y_math.append(tanh_math(i))

ax1=plt.subplot(2,1,1)
ax2=plt.subplot(2,1,2)

# ax1.set_ylim(0,1) #Y軸の範囲
ax1.plot(x,y_np,"k")
ax2.plot(x,y_math,"k")




plt.show()
