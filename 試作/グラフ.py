import math 
import matplotlib.pyplot as plt

# pyplotモジュールを"plt"という名前でインポートする
x_a=[]
y_a=[]

for x in range(-540,540):
    y=0
    for n in range(0,1000):
        sin_a=math.sin((2*n+1)*math.radians(x))/(2*n+1)
        y=y+4/math.pi*sin_a
    x_a.append(x)
    y_a.append(y)



plt.plot(x_a, y_a, color="k") # 点列(x,y)を黒線で繋いだプロット
plt.show() # プロットを表示
