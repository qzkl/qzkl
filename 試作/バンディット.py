import math
import random
import matplotlib.pyplot as plt

card=[1500,1000]
num=len(card)
a=0.5
a1=0.05
b1=0.004
S=[[] for b in range(num)]
Q=[[] for b in range(num)]
P=[[] for b in range(num)]
t0=[0]*num
q=[]*num
x=[]
a_1=[]
At=Bt=0

for i0 in range(100):
    for i in range(100):
        d=random.random()
        if d<=a:
            rt=int(card[0]*random.random())
            S[0].append(rt)
            S[1].append("")
            qa=At+a1*(rt-At)
            qb=Bt
            At=qa

            Q[0].append(qa)
            
            Q[1].append(qb)
            pa=math.exp(b1*qa)
            pb=math.exp(b1*qb)
            aa=pa/(pa+pb)
            ab=pb/(pa+pb)
            P[0].append(aa)
            P[1].append(ab)
            a=aa
        else:
            rt=int(card[1]*random.random())
            S[0].append("")
            S[1].append(rt)
            qa=At
            qb=Bt+a1*(rt-Bt)
            Q[0].append(qa)
            Bt=qb
            Q[1].append(qb)
            pa=math.exp(b1*qa)
            pb=math.exp(b1*qb)
            aa=pa/(pa+pb)
            ab=pb/(pa+pb)

            P[0].append(aa)
            P[1].append(ab)
            a=aa
    a_max=max(P[0])
    a_1.append(a_max)
    x.append(i0)
    S=[[] for b in range(num)]
    Q=[[] for b in range(num)]
    P=[[] for b in range(num)]


ax1=plt.subplot(1,1,1)

ax1.set_ylim(0,1) #Y軸の範囲
ax1.plot(x,a_1,"k")

# plt.plot(x,P[0],"k")
# plt.plot(x,P[1],"b")


plt.show()

