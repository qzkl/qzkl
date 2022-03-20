from math import radians
import tkinter
import numpy as np
import random

root=tkinter.Tk()
root.title("坂")
root.geometry("1200x1500")
cv=tkinter.Canvas(root,width=1500,height=1000)
cv.place(x=0,y=0)

g=9.80665
# 摩擦係数
u=0.2
# コマ数
ta=0.01

def draw_circle(x,y,r,color):
    x1=x-r
    x2=x+r
    y1=y-r
    y2=y+r
    return cv.create_oval(x1,y1,x2,y2,fill=color)
    
def draw_load(ln,rad,color):
    t=0
    di=[]
    x=ln*np.cos(np.radians(rad))
    y=ln*np.sin(np.radians(rad))
    
    origin=[100,500-y]
    ln1=1000-x
    
    cv.create_line(origin[0],origin[1],origin[0]+x,origin[1]+y,
                   origin[0]+x+ln1,origin[1]+y,fill=color)
    root.after(30,draw_load)    
    y0=origin[1]+y
    
    vt=0
    x2=[]
    
    def canvs_ball():
        nonlocal t,di,y0,vt,x2
        
        # 球の大きさ
        r=10
        
        
        if len(di)>0:
            cv.delete(di[0])
            di=[]
        
        # 加速度
        a1=g*np.sin(np.radians(rad))-u*g*np.cos(np.radians(rad))
        # 速度
        vt=a1*t
        
        if vt<0:
            lt1=0
        else:
            lt1=(a1*t**2)/2
        
        # 斜面の移動座標   
        x1=origin[0]+r*np.cos(np.radians(rad))+lt1*np.cos(np.radians(rad))
        y1=origin[1]-r*np.sin(np.radians(rad))+lt1*np.sin(np.radians(rad))
        # print(x1,y1)
        
        # 直線の移動座標
        if y0<y1+r:
            
            tb=np.sqrt(2*(ln-r)/a1)
            va=tb*a1
            a2=-u*g
            t2=(t-tb)
            lt2=(a2*t2**2)/2+va*t2
            x1=origin[0]+x+lt2
            y1=origin[1]+y-r
            x2.append(x1)
            abc=max(x2)-x2[-1]
            if abc>0:
                
                t=-1*ta
                x2.clear()
               
          
        id=draw_circle(x1,y1,r,color)
        di.append(id)
        if x1>1000 :
            t=0
            x2.clear()
            
        
        else:
            t+=ta
        root.after(1,canvs_ball)

    return canvs_ball


ball=draw_load(200,45,"#ff0000")
ball2=draw_load(200,20,"#000000")
ball3=draw_load(100,70,"#ff00f0")

ball()
ball2()
ball3()
root.mainloop()
    