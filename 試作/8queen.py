yoko=[1,2,3,4,5,6,7,8]

for a in range(1,9):
    na="l"+str(a)
    na=[0 for b in range(1,9)]
    # print(na)

def co(line,yo):
    for a in yo:
        na="l"+str(line)
        na[a]=1
        line +=1
        del yo[a]
        if len(yo)>0:
            co(line,yo)
        else:
            for a in range(1,9):
                na="l"+str(a)
                print(na)

r=co(1,yoko)
