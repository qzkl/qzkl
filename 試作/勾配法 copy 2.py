import math
import random
import matplotlib.pyplot as plt

g=4
x=[[] for b in range(g)]
y=[[] for b in range(g)]
a0=-0.8
b0=1.9
nn=[0.05,0.2,0.5,0.8]


class Stp:
    def __init__(self,x0,y0,n):
        self.x=x0
        self.y=y0
        self.n=n

    def stpf(self):
        z_0=math.exp(0.5*a**2+0.2*b**2)
        x_0=-1*a*math.exp(0.5*a**2+0.2*b**2)
        y_0=-1*0.4*b*math.exp(0.5*a**2+0.2*b**2)
        x_1=a+n*x_0
        y_1=b+n*y_0
        z_1=math.exp(0.5*x_1**2+0.2*y_1**2)
        x[i].append(x_1)
        y[i].append(y_1)
        if abs(z_0-z_1)<10**-6:
            return x_1,y_1,len(x)
        else:
            return stp(x_1,y_1,n,i)

def stp(a,b,n,i):
    z_0=math.exp(0.5*a**2+0.2*b**2)
    x_0=-1*a*math.exp(0.5*a**2+0.2*b**2)
    y_0=-1*0.4*b*math.exp(0.5*a**2+0.2*b**2)
    x_1=a+n*x_0
    y_1=b+n*y_0
    z_1=math.exp(0.5*x_1**2+0.2*y_1**2)
    x[i].append(x_1)
    y[i].append(y_1)

    if abs(z_0-z_1)<10**-6:
        return x_1,y_1,len(x)
    else:
        return stp(x_1,y_1,n,i)

i=0
for n1 in nn:
    x[i].append(a0)
    y[i].append(b0)
    
    f=stp(a0,b0,n1,i)
    i+=1


plt.subplots_adjust(wspace=0.4, hspace=0.6)
ax1=plt.subplot(2,2,1)
ax2=plt.subplot(2,2,2)
ax3=plt.subplot(2,2,3)
ax4=plt.subplot(2,2,4)

aa=[ax1,ax2,ax3,ax4]

i=0
for ax in aa:
    ax.set_title(len(x[i]), fontsize = 11)
    ax.set_xlim(-2,2) #x軸の範囲
    ax.set_ylim(-2,2) #Y軸の範囲
    ax.plot(x[i],y[i],"k")
    i+=1

plt.show()
# ax1.plot(x,a_1,"k")

# # plt.plot(x,P[0],"k")
# # plt.plot(x,P[1],"b")


# plt.show()