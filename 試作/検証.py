import matplotlib.pyplot as plt
import math 
# pyplotモジュールを"plt"という名前でインポートする
x_a=[]
y_a=[]

for x in range(-180,180):

    sin_a=math.sin(math.radians(x))
    y=sin_a
    x_a.append(x)
    y_a.append(y)



plt.plot(x_a, y_a, color="k") # 点列(x,y)を黒線で繋いだプロット
plt.show() # プロットを表示