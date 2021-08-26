import math
import random
import matplotlib.pyplot as plt

card=[2000,1000]
num=len(card)
c=0.5
a1=0.05
b1=0.004
S=[[] for b in range(num)]
Q=[[] for b in range(num)]
P=[[] for b in range(num)]
t0=[0]*num
t1=p1=c1=[0]*num
q1=[0]*num
x=[]
a_1=[]


def drow(x):
    
    for i in range(num):
        if i==x:
            rt=int(card[x]*random.random())
        else:
            rt=0
        S[i].append(rt)
        c=t0[i]+a1*(rt-t0[i])
        Q[i].append(c)
        q1[i]=c
        t0[i]=c
        

    for i in range(num):

        t1[i]=math.exp(b1*q1[i])

    for i in range(num):
        c=t1[i]/(sum(t1))
        P[i].append(c)
    
    return t1[0]/(sum(t1))

# for i0 in range(100):
for i in range(100):
    d=random.random()
    if d<=c:
        c=drow(0)
    else:
        c=drow(1)
    x.append(i)
    # a_max=max(P[0])
    # a_1.append(a_max)
    # x.append(i0)
    # S=[[] for b in range(num)]
    # Q=[[] for b in range(num)]
    # P=[[] for b in range(num)]


# ax1=plt.subplot(1,1,1)

# ax1.set_ylim(0,1) #Y軸の範囲
# ax1.plot(x,a_1,"k")

plt.plot(x,P[0],"k")
plt.plot(x,P[1],"b")


plt.show()

