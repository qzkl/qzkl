pos=[0]*8
flag_a=[False]*8
flag_b=[False]*15
flag_c=[False]*15
x=[]

def put():
    x.append(1)
    print(len(x))
    for i in range(8):
        
        print(f'{pos[i]:2}',end=" ")
        
    print()

def set(i):
    for j in range(8):
        if not flag_a[j] and not flag_b[7-i+j] and not flag_c[14-i-j]:
            pos[i]=j
            if i==7:
                put()
            else:
                flag_a[j]=flag_b[7-i+j]=flag_c[14-i-j]=True
                set(i+1)
                flag_a[j]=flag_b[7-i+j]=flag_c[14-i-j]=False

set(0)
