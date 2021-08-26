import matplotlib.pyplot as plt
import math 
import numpy as np

# pyplotモジュールを"plt"という名前でインポートする
num=4
x_1=[]
y_1=[[] for b in range(num)]


for x in np.arange(0,10,0.001):
    a=0
    ex=math.exp(-x)
    sin=math.sin(2*math.pi*x)
    esin=ex*sin

    sin=[ex,sin,esin]


    x_1.append(x)
    for sin_x in sin:
        y_1[a].append(sin_x)
        a+=1

ax1=plt.subplot(2,2,1)
ax2=plt.subplot(2,2,2)
ax3=plt.subplot(2,2,3)
# ax4=plt.subplot(2,2,4)

ax=[ax1,ax2,ax3]
color=["k","b","r"]
# ax1.plot(x_1,y_1,"k")
# ax2.plot(x_1,y_2,"b")
# ax3.plot(x_1,y_3,"r")
# ax4.plot(x_1,y_4,"g")

for ax_x,y_x,color_x in zip(ax,y_1,color):
    ax_x.set_xlim(0,5) #X軸の範囲
    ax_x.set_ylim(-2,2) #Y軸の範囲
    ax_x.plot(x_1,y_x,color_x)


plt.show()