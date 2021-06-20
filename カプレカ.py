import sys
n=list()
num_a=input("桁数を入力してください")
num_ab=int(num_a)
flag=0

for i in range(num_ab):
    a=input("{}番目".format(i+1))
    n.append(a)
    if i==0:
        m1=a
    else:
        m2=a
    
    if i>=2 and m1==m2:
        flag=+1
    

if flag==num_ab:
    print("全て同じ数字です")
    sys.exit()



def num(m,ab):
    msum=0
    nsum=0
    m.sort()
    for i in range(ab):
        a=int(m[i])*10**(ab-i-1)
        msum=msum+a
    m.reverse()
    for i in range(ab):
        a=int(m[i])*10**(ab-i-1)
        nsum=nsum+a
    
    return nsum-msum

def func_ex(r,ab):
    nlist=list()
    for i in str(r):
        nlist.append(i)
    return num(nlist,ab)
    
    
def func_e(aa,ab,ac):
    if aa==ab:
        return aa
    else:
        aa=ab
        ab=func_ex(ab,ac)
        # print(ab)
        return func_e(aa,ab,ac)


ex1=num(n,num_ab)
ex2=func_ex(ex1,num_ab)
print(ex2)
ex3=func_e(ex1,ex2,num_ab)
print(ex3)









