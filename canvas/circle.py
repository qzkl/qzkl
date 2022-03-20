import tkinter
import numpy as np
import random

root=tkinter.Tk()
root.title("円")
root.geometry("1200x1500")
cv=tkinter.Canvas(root,width=1500,height=1000)
cv.place(x=0,y=0)

num=10
len=10
len1=0
x=[0 for i in range(1,num+1)]
y=[0 for i in range(1,num+1)]


angle=0
angle1=0
angle_c=0.1

def draw_circle(x,y,r):
    x1=x-r
    x2=x+r
    y1=y-r
    y2=y+r
    cv.create_oval(x1,y1,x2,y2,fill="#ff0000")



def draw_oval():
    global angle
    global angle1
    global len,x,y,x1,y1,len1
    
    

    cv.delete("all")
    angle1=angle1+angle_c
    len1+=1
    len=2**len1
    
    
    for i in range(0,num):
        if len>200:
            len1=0
            for a in range(0,num):
                x[a]=random.randint(100,1000)
                y[a]=random.randint(100,1000)
            

        draw_circle(x[i],y[i],len)
        
    
    # angle=np.sin(angle1)
    # len=np.sin(angle1)*len1
    
    root.after(100,draw_oval)

draw_oval()
root.mainloop()   