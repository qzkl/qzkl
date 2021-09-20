import matplotlib.pyplot as plt
import math 
import numpy as np

a=10

x_a=[]
y_a=[]


for x in np.arange(-20,20,0.01):
    y=a/(a**2+x**2)

    x_a.append(x)
    y_a.append(y)

plt.plot(x_a, y_a, color="k") # 点列(x,y)を黒線で繋いだプロット
plt.show() # プロットを表示