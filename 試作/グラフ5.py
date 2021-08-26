import matplotlib.pyplot as plt
import math 
import numpy as np

# pyplotモジュールを"plt"という名前でインポートする
m=[2,4,20000]
num=len(m)
x_1=[]
y_1=[[] for b in range(num)]
a=0
for m_x in m:
    
    for x in np.arange(-100,100,0.01):
        if x==0:
            x=0
            yn=1/m_x
            continue
        else:
            yn=math.sin(x*math.pi/m_x)/(x*math.pi)


        if a==0:
            x_1.append(x)
        y_1[a].append(yn)
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
    # ax_x.set_xlim(-2,2) #X軸の範囲
    # ax_x.set_ylim(-1,1) #Y軸の範囲
    ax_x.plot(x_1,y_x,color_x)


plt.show()