from math import radians
import tkinter
import numpy as np
import random

root=tkinter.Tk()
root.title("衝突")
root.geometry("1200x1500")
cv=tkinter.Canvas(root,width=1500,height=1000)
cv.place(x=0,y=0)

g=9.80665
# 摩擦係数
u=0.2
# コマ数
ta=0.005

def draw_circle(x,y,r,color):
    x1=x-r
    x2=x+r
    y1=y-r
    y2=y+r
    return cv.create_oval(x1,y1,x2,y2,fill=color)
    
def draw_load(ln,v0,rad,rad2,color):
    t=0
    di=[]
    x=ln*np.cos(np.radians(rad))
    y=ln*np.sin(np.radians(rad))
    xend=ln*np.cos(np.radians(rad2))
    yend=ln*np.sin(np.radians(rad2))
    
    origin=[100,500-y]
    ln1=1000-x-xend
    end=[1000,500-yend]
    
    
    cv.create_line(origin[0],origin[1],origin[0]+x,origin[1]+y,
                   origin[0]+ln1,origin[1]+y,end[0],end[1],fill=color)
    root.after(30,draw_load)    
    
    y0=origin[1]+y
    x0=origin[0]+ln1
    
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
        vt=v0+a1*t
        
        if vt<0:
            lt1=0
        else:
            lt1=(a1*t**2)/2+v0*t
        
        # 斜面の移動座標   
        x1=origin[0]+r*np.cos(np.radians(rad))+lt1*np.cos(np.radians(rad))
        y1=origin[1]-r*np.sin(np.radians(rad))+lt1*np.sin(np.radians(rad))
        # print(x1,y1)
        
        # 直線の移動座標
        if y0<y1+r:
            
            tb=(-2*v0+np.sqrt(4*v0**2+8*a1*(ln-r)))/(2*a1)
            va=tb*a1+v0
            a2=-u*g
            t2=(t-tb)
            vat=va+a2*t2
            lt2=(a2*t2**2)/2+va*t2
            x1=origin[0]+x+lt2
            y1=origin[1]+y-r
            if vat<=0:
                t+=-1*ta
                
               
          
        id=draw_circle(x1,y1,r,color)
        di.append(id)
        
        if t>30 :
            t=0
        else:
            t+=ta
        root.after(1,canvs_ball)

    return canvs_ball


ball=draw_load(200,30,0,0,"#ff0000")
ball2=draw_load(200,60,0,0,"#000000")
# ball3=draw_load(100,70,"#ff00f0")

ball()
ball2()
# ball3()
root.mainloop()
    