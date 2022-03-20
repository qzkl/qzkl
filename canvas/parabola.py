import tkinter
import numpy as np
import random

root=tkinter.Tk()
root.title("放物線")
root.geometry("1200x1500")
cv=tkinter.Canvas(root,width=1500,height=1000)
cv.place(x=0,y=0)

g=9.80665

def draw_circle(x,y,r):
    x1=x-r
    x2=x+r
    y1=y-r
    y2=y+r
    return cv.create_oval(x1,y1,x2,y2,fill="#ff0000")

def draw_parab(v,rad):
    t=0
    i=0
    di=[]
    tt=0.5
    
    def canvas_parab():
        nonlocal t,i,di
        
        
        x=v*np.cos(np.radians(rad))*t
        y=v*np.sin(np.radians(rad))*t-(1/2)*g*t**2
        
        ln=len(di)
        if y<0:
            for xi in range(0,ln):
                cv.delete(di[xi])
            di=[]
            t=0
        elif t==0 and i>1:
            cv.delete(di[-1])
            
            t+=tt
        else:
            t+=tt
        # t+=0.5    
        # cv.delete("all")
        # if y<0:
        #     t=0
        
        id=draw_circle(x,500-y,20)
        i+=1
        di.append(id)
        
        
        root.after(60,canvas_parab)
        
        
    return canvas_parab

pra=draw_parab(100,60)
pra2=draw_parab(100,45)
pra3=draw_parab(100,30)
pra()
pra2()
pra3()

root.mainloop()
    