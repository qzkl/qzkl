yoko=[1,2,3,4,5,6,7,8]
tate=[]



for a in range(1,9):
    na="l"+str(a)
    na=[0 for b in range(1,9)]
    tate.append(na)
# [print(l) for l in tate]

def co(line,yo,l=0):
    for a in yo:
        line[l][a-1]=1
        l +=1
        yo.remove(a)
        if len(yo)>0:
            co(line,yo,l)
        else:
            [print(l) for l in line]

r=co(tate,yoko)
