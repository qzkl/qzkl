import matplotlib.pyplot as plt
import math 
import numpy as np

# pyplotモジュールを"plt"という名前でインポートする
num=4
x_1=[]
y_1=[[] for b in range(num)]
# sin=[sin_a,sin_b,sin_c,sin_d]
# ax=[ax1,ax2,ax3,ax4]

for x in np.arange(-2,2,0.001):
    a=0
    sin_b=2*math.sin(2*math.pi*x)
    sin_c=10*math.sin(7*math.pi*x)
    sin_d=3*math.sin(10*math.pi*x)
    sin_a=sin_b+sin_c+sin_d
    sin=[sin_a,sin_b,sin_c,sin_d]


    x_1.append(x)
    for sin_x in sin:
        y_1[a].append(sin_x)
        a+=1

ax1=plt.subplot(2,2,1)
ax2=plt.subplot(2,2,2)
ax3=plt.subplot(2,2,3)
ax4=plt.subplot(2,2,4)

ax=[ax1,ax2,ax3,ax4]
color=["k","b","r","g"]
# ax1.plot(x_1,y_1,"k")
# ax2.plot(x_1,y_2,"b")
# ax3.plot(x_1,y_3,"r")
# ax4.plot(x_1,y_4,"g")

for ax_x,y_x,color_x in zip(ax,y_1,color):
    ax_x.plot(x_1,y_x,color_x)


plt.show()