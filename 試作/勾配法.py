import math
import random
import matplotlib.pyplot as plt


x=[]
y=[]
a0=-0.8
b0=1.9
x.append(a0)
y.append(b0)



n=0.2
def stp(a,b):
    z_0=math.exp(0.5*a**2+0.2*b**2)
    x_0=-1*a*math.exp(0.5*a**2+0.2*b**2)
    y_0=-1*0.4*b*math.exp(0.5*a**2+0.2*b**2)
    x_1=a+n*x_0
    y_1=b+n*y_0
    z_1=math.exp(0.5*x_1**2+0.2*y_1**2)
    x.append(x_1)
    y.append(y_1)

    if abs(z_0-z_1)<10**-6:
        return x_1,y_1,len(x)
    else:
        return stp(x_1,y_1)

f=stp(a0,b0)

print(f)

plt.plot(x,y,"k")

plt.show()


# ax1=plt.subplot(1,1,1)

# ax1.set_ylim(0,1) #Y軸の範囲
# ax1.plot(x,a_1,"k")

# # plt.plot(x,P[0],"k")
# # plt.plot(x,P[1],"b")


# plt.show()