import matplotlib.pyplot as plt
import math 
import numpy as np
# pyplotモジュールを"plt"という名前でインポートする
x_a=[]
y_a=[]
a=2
h=0.1
sm=0

for x in np.arange(-20000,20000,h):

    yn=a/(a**2+x**2)
    ym=a/(a**2+(x+h)**2)
    s=(yn+ym)*h/2
    sm=sm+s

print(sm)



