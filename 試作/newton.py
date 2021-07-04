import math

def newton(x):
    km=100
    er1=10**-10
    x1=x
    a=x
    for i in range(km):
        x2=x1-0.5*(x1**2-a)
        er=abs(x2-x1)
        if er<er1:
            return x2,er,i
        else:
            x1=x2 


x,er,i=newton(2)

print(x,er,i)
print(math.sqrt(2))