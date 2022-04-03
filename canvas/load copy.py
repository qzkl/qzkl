from math import radians
import tkinter
import numpy as np
import random

root=tkinter.Tk()
root.title("直線")
root.geometry("1200x1500")
cv=tkinter.Canvas(root,width=1500,height=1000)
cv.place(x=0,y=0)

g=9.80665
# 摩擦係数
u=0.2
# コマ数
ta=0.1

def draw_circle(x,y,r,color):
    x1=x-r
    x2=x+r
    y1=y-r
    y2=y+r
    return cv.create_oval(x1,y1,x2,y2,fill=color)
    
def draw_load(y,v0,color):
    t=0
    di=[]
    di2=[]
        
    origin=[100,y]
    ln1=1000
    
    
    cv.create_line(origin[0],origin[1],origin[0]+ln1,origin[1],
                   fill=color)
    cv.create_text(origin[0]+100,origin[1]-50,text="V="+str(v0),
                    font=('Times New Roman', 50))
    # root.after(30,draw_load)    
    
    vt=0
    x2=[]
    t=0
    lt2=0
    i=0
    
    
    def canvs_ball():
        nonlocal t,di,vt,x2,lt2,i,di2
        
        # 球の大きさ
        r=10

        if len(di)>0 and int(t*10%20)!=0:
            cv.delete(di[-1])
            # di=[]
       
        # 直線の移動座標
 
        a2=-u*g
        va=t*a2+v0
        
        
        
        if t==0:
            lt1=(a2*t**2)/2+v0*t
            
        else:
            lt1=(a2*t**2)/2+v0*t-((a2*(t-ta)**2)/2+v0*(t-ta))
        
        if va<=0:
            lt1=0
            i+=1
            
        lt2+=lt1
        
        x1=origin[0]+lt2
        y1=origin[1]-r
        
        if i==1:
            ren=x1-origin[0]
            id2=cv.create_text(x1,y1+30,text=str(ren),font=('Times New Roman', 20))
            di2.append(id2)
            
        
                
               
          
        id=draw_circle(x1,y1,r,color)
        di.append(id)
        
        if t>=60 :
            t=0
            x1=origin[0]
            y1=origin[1]-r
            lt2=0
            cv.delete(di2[0])
            for i in di:
                cv.delete(i)
            di=[]
            di2=[]
            i=0
        else:
            t+=ta
        root.after(10,canvs_ball)

    return canvs_ball


ball=draw_load(200,60,"#ff0000")
ball2=draw_load(400,30,"#f000f0")
# ball3=draw_load(100,70,"#ff00f0")

ball()
ball2()
# ball3()
root.mainloop()
    