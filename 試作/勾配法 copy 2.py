import math
import random
import matplotlib.pyplot as plt

class Stp:
    def __init__(self,x0,y0,n):
        self.x=x0
        self.y=y0
        self.n=n
        self.xl=[]
        self.yl=[]
        self.xl.append(self.x)
        self.yl.append(self.y)

    
    def stpf(self,a,b):
        
        x_0=-1*a*math.exp(0.5*a**2+0.2*b**2)
        y_0=-1*0.4*b*math.exp(0.5*a**2+0.2*b**2)
        x_n=a+self.n*x_0
        y_n=b+self.n*y_0
        z_n=math.exp(0.5*x_n**2+0.2*y_n**2)
        return x_n,y_n,z_n

    def reslut(self):
        z_0=math.exp(0.5*self.x**2+0.2*self.y**2)
        x_1=self.x=self.stpf(self.x,self.y)[0]
        y_1=self.y=self.stpf(self.x,self.y)[1]
        z_1=self.stpf(self.x,self.y)[2]
        self.xl.append(x_1)
        self.yl.append(y_1)

        if abs(z_0-z_1)<10**-6:
            return self.xl,self.yl,len(self.xl)
        else:
            self.stpf(x_1,y_1)
            return self.reslut()

d=Stp(-0.9,1.8,0.1)


plt.plot(d.reslut()[0],d.reslut()[1],"k")
plt.show()