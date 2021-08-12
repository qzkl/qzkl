import matplotlib.pyplot as plt
import math 
# pyplotモジュールを"plt"という名前でインポートする
x_a=[]
y_a=[]

for x in range(-180,180):
    y=0
    for n in range(1,10000):
        sin_a=math.sin((n)*math.radians(x))*(2/n)*(-1)**(n+1)
        y=y+sin_a
    x_a.append(x)
    y_a.append(y)



plt.plot(x_a, y_a, color="k") # 点列(x,y)を黒線で繋いだプロット
plt.show() # プロットを表示