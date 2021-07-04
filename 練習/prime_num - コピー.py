import time
import sys
# import resource
sys.setrecursionlimit(10000000)
start = time.time()
pnum=[2]

def num(a,n=0):
    if a%pnum[n]==0:
        pass
    elif n==len(pnum)-1:
        pnum.append(a)
    elif a/pnum[n]<=2:
        pnum.append(a)
        print("{}:{}".format(len(pnum),a))
    else:
        n+=1
        return num(a,n)

# def prime(n):
#     for i in range(3,n):
#         if i%2==0:
#             continue
#         # elif i>5 and i%5==0:
#         #     continue
#         else:

#         # print("{}:{}".format(i,b))

def make_pnum(a):
    path_w = 'C:/Users/nakahashi/test/prime_num.txt'
    print(pnum)
    s=[str(n) for n in pnum]
    with open(path_w, mode='w') as f:
        f.write('\n'.join(s))

def prime_n(a):
    
    path_w = 'C:/Users/nakahashi/test/prime_num.txt'
    with open(path_w) as f:
        s = [s.strip() for s in f.readlines()]
        r=[int(n) for n in s ]
        t=[x for x in r if x<=a]
    return t


for abc in range(3,1001):
    aac=num(abc)
    
f=prime_n(2000)
print(f)

# ab=f[5]
# print(ab)
elapsed_time = time.time() - start
