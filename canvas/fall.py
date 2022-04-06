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

# コマ数
ta=0.03

def draw_circle(x,y,r,color):
    x1=x-r
    x2=x+r
    y1=y-r
    y2=y+r
    return cv.create_oval(x1,y1,x2,y2,fill=color)

def draw_load(x,H,rball,k,m,t_ori,t_end,color):
    
    by=H/hei
    t=0
    di=[]
    di2=[]
    
    origin=[x,0]
    line=hei-100
    
    
    cv.create_line(0,line,wid,line,fill=color)
    
    cv.create_text(300,200,text="H="+str(int(hei*by)),
                    font=('Times New Roman', 30))
     
    
    vt=0
    
    t=0
    lt2=0
    i=0
    it=1
    
    
    T=np.sqrt(m/(g*k))
    V=np.sqrt(m*g/k)
    
    y_frm=H/by/10
    
    def canvs_ball():
        
        nonlocal t,di,vt,lt2,i,di2,it
        
        # 球の大きさ
        r=rball
       
        # 直線の移動座標
 
        
        va=V*np.tanh(t/T)

        if t==0:
            lt1=V*T*np.log(np.cosh(t/T))
            
        else:
            lt1=V*T*np.log(np.cosh(t/T))-(V*T*np.log(np.cosh((t-ta)/T)))
        
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
           id2=cv.create_text(x1+200,y1,text=str(round(t,2)),font=('Times New Roman', 20)) 
        #    elapsed_time = time.time() - start
        #    id2=cv.create_text(x1-100,y1,text=str(round(elapsed_time,2)),font=('Times New Roman', 20))
        
        if len(di)>0 and round(y1,2)<round(y_frm,2)*it and va>0 :
            cv.delete(di[-1])
            del di[-1]
        elif va>0:  
            id2=cv.create_text(x1+50,y1,text=str(round(va,2)),font=('Times New Roman', 20))
            di2.append(id2)
            
            it+=1
        
           
        id=draw_circle(x1,y1,r,color)
        if va>0:
            di.append(id)
        
        if t>=t_end+10:
            
            x1=origin[0]
            y1=origin[1]
            
            
            
            cv.delete("all")
            cv.create_line(0,line,wid,line,fill=color)
            cv.create_text(300,200,text="H="+str(int(hei*by)),
                    font=('Times New Roman', 30))
            di=[]
            di2=[]
            t=lt2=i=it=0
            
        else:
            t+=ta
        root.after(20,canvs_ball)

    return canvs_ball

tlist=[]

H=1000
rball1=10
k1=0.4
m1=70
t1=np.sqrt(m1/g/k1)*np.arccosh(np.exp(H*k1/m1))
tlist.append(t1)

rball2=10
k2=0.4
m2=100
t2=np.sqrt(m2/g/k2)*np.arccosh(np.exp(H*k2/m2))
tlist.append(t2)

T=max(tlist)


ball=draw_load(500,H,rball1,k1,m1,t1,T,"#ff0000")
ball2=draw_load(800,H,rball2,k2,m2,t2,T,"#f000f0")

ball()
ball2()

root.mainloop()