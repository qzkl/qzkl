#READ+WRITE+TALK=SKILL
import itertools
import time
start = time.time()

a="READ"
b="WRITE"
c="TALK"
d="SKILL"

num_r=dict()
spel=[a,b,c,d]

alf=[]

for word in spel:
    for alf_n in word:
        alf.append(alf_n)

alf_s=set(alf)
print(alf_s)

num=[0,1, 2, 3,4,5,6,7,8,9]

my_dic=dict()

i=0
for num_x in itertools.permutations(num,10):
    i=0
    for aac in alf_s:
        my_dic[aac]=num_x[i]
        i+=1
        
    for word2 in spel:
        i=1
        s0=0
        for spl2 in word2:
            
            
            num_s=my_dic[spl2]
            
            s=10**(len(word2)-i)*num_s+s0
            s0=s
            if len(word2)-i==0:
                num_r[word2]=s
            i+=1

    spel2=[]
    for x in spel:
        spel2.append(num_r[x])
        
    # print(spel2)
    flag=0
    if spel2[0]+spel2[1]+spel2[2]==spel2[3]:
        flag+=1
    flag2=True
    for i in range(0,len(spel)):
        a1=len(spel[i])
        a2=len(str(spel2[i]))
        if a1!=a2:
            flag2=False
    if flag2==True:
        flag+=1
    
    if flag==2:
        print(num_r)

elapsed_time = time.time() - start
print(elapsed_time)

