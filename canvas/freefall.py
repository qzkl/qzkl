from math import radians
import tkinter
import numpy as np
import random
import time
start = time.time()

root=tkinter.Tk()
root.title("直線")
wid=root.winfo_screenwidth()
hei=root.winfo_screenheight()
root.geometry("{}x{}".format(wid,hei))
cv=tkinter.Canvas(root,width=wid,height=hei)
cv.place(x=0,y=0)

g=9.80665
# 摩擦係数
u=0.2
# コマ数
ta=0.03

def draw_circle(x,y,r,color):
    x1=x-r
    x2=x+r
    y1=y-r
    y2=y+r
    return cv.create_oval(x1,y1,x2,y2,fill=color)

def draw_load(v0,H,rball,color):
    
    by=H/hei
    t=0
    di=[]
    di2=[]
    
    origin=[500,0]
    line=hei-100
    
    
    cv.create_line(0,line,wid,line,fill=color)
    
    cv.create_text(origin[0]-200,origin[1]+200,text="H="+str(int(hei*by)),
                    font=('Times New Roman', 30))
    # root.after(30,draw_load)    
    
    vt=0
    # x2=[]
    t=0
    lt2=0
    i=0
    it=1
    a2=g
    tta=(-2*0+np.sqrt(4*a2*2*hei*by))/(2*a2)
    
    def canvs_ball():
        
        nonlocal t,di,vt,lt2,i,di2,it
        
        # 球の大きさ
        r=rball
       
        # 直線の移動座標
 
        
        va=t*a2+v0
      
        if t==0:
            lt1=(a2*t**2)/2+v0*t
            
        else:
            lt1=(a2*t**2)/2+v0*t-((a2*(t-ta)**2)/2+v0*(t-ta))
        
        if va<=0:
            va=0
            lt1=0
            
            
        lt2+=lt1*line/H
        
        x1=origin[0]
        y1=origin[1]+lt2
        
        if y1>=line-r:
            y1=line-r
            va=0
            i+=1
        
        if i==1:
           id2=cv.create_text(x1+100,y1,text=str(round(t,2)),font=('Times New Roman', 20)) 
        #    elapsed_time = time.time() - start
        #    id2=cv.create_text(x1-100,y1,text=str(round(elapsed_time,2)),font=('Times New Roman', 20))
        
        if len(di)>0 and round(t,2)<round(tta/10,2)*it and va>0 :
            cv.delete(di[-1])
            del di[-1]
        elif va>0:  
            id2=cv.create_text(x1+50,y1,text=str(round(va,2)),font=('Times New Roman', 20))
            di2.append(id2)
            
            it+=1
        
           
        id=draw_circle(x1,y1,r,color)
        if va>0:
            di.append(id)
        
        if t>=tta+5:
            
            x1=origin[0]
            y1=origin[1]
            
            
            
            cv.delete("all")
            cv.create_line(0,line,wid,line,fill=color)
            cv.create_text(origin[0]-200,origin[1]+200,text="H="+str(hei*by),
                    font=('Times New Roman', 30))
            di=[]
            di2=[]
            t=lt2=i=it=0
            
        else:
            t+=ta
        root.after(20,canvs_ball)

    return canvs_ball

ball=draw_load(0,10000,10,"#ff0000")
ball()

root.mainloop()