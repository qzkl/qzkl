import tkinter
import numpy as np
import random

root=tkinter.Tk()
root.title("波動")
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

def draw_sin(a,t):
    
    i=0
    di=[]
    tt=0.5
    
    def canvas_sin():
        nonlocal t,i,di,tt
        cv.delete("all")
        
        for xi in range(0,1000,t):
            x=xi
            y1=a*np.cos(np.radians(xi+tt))
            y2=a*np.sin(np.radians(i*xi+tt))
            y=y1+y2
            draw_circle(x,500-y,20)
       
        tt+=10
        i+=0.05   
        root.after(100,canvas_sin)
        
        
    return canvas_sin

pra=draw_sin(100,10)

pra()


root.mainloop()
    