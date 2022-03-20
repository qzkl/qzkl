
import tkinter
import numpy as np
import time

# グローバル変数を変更する場合globalの宣言が必要
# 読み取るだけなら宣言は不要

root=tkinter.Tk()
root.title("回転")
root.geometry("1000x1000")
cv=tkinter.Canvas(root,width=1000,height=1000)
cv.place(x=0,y=0)



def draw_sq(x,y,len,rad,t,color,n):
    len1=len 
    i=0
    # n=8
    di=[]
    
    # color="#ff00f0"
    
    def rotate_sq():
        nonlocal rad,len,i
        c=np.array([x,y])
        
        
        p1=c+np.array([len/2,len/2])
        p2=c+np.array([len/2,-len/2])
        p3=c+np.array([-len/2,-len/2])
        p4=c+np.array([-len/2,len/2])
        
        # c=np.array([x+len1/2,y+len1/2])
        
        R=np.array([[np.cos(rad),-np.sin(rad)],
                    [np.sin(rad), np.cos(rad)]])
        
        r1=R@(p1-c)+c
        r2=R@(p2-c)+c
        r3=R@(p3-c)+c
        r4=R@(p4-c)+c
        
        i+=1
        
        if i>n:
            cv.delete(di[i-(n+1)])
        
        id=cv.create_line(r1[0],r1[1],r2[0],r2[1],
                    r3[0],r3[1],r4[0],r4[1],
                    r1[0],r1[1],fill=color)
        
        di.append(id)        
        
        
        
        rad+=t 
        len=np.sin(rad)*len1 
        
        root.after(30,rotate_sq)
      
    return rotate_sq

r=0
len=300
rad=0

    
sq1=draw_sq(300,300,len,r,0.05,"#ff00f0",10)
sq2=draw_sq(400,400,len,r,0.05,"#ff0000",5)
sq3=draw_sq(500,400,len*2,r,-0.05,"#00000f",15)
sq1()
sq2()
sq3()


root.mainloop()


