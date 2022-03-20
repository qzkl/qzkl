import tkinter
import numpy as np

root=tkinter.Tk()
root.title("振り子")
root.geometry("1200x1500")
cv=tkinter.Canvas(root,width=1500,height=1000)
cv.place(x=0,y=0)

g=9.80665
# 摩擦係数
u=0.2
# コマ数
ta=0.01

r=30
def draw_circle(x,y,r,color):
    x1=x-r
    x2=x+r
    y1=y-r
    y2=y+r
    return cv.create_oval(x1,y1,x2,y2,fill=color)

def draw_pendulum(ln,rad,color):
    t=0
    di=[]

    radt=0.05
    if rad<90:
        rad0=180-rad
        rad1=rad0
    
    else:
        rad0=rad
        rad1=180-rad0
     
    def canvas_pendulum():
        nonlocal rad0,rad1,rad
        
        # H=g*ln*(1-np.cos(np.radians(rad0)))
        # H1=g*ln*(1-np.cos(np.radians(rad)))
        # V=np.sqrt(2*(H-H1))
        
        x=ln*np.cos(np.radians(rad))
        y=ln*np.sin(np.radians(rad))
        origin=[600,0]
        x1=origin[0]+(ln+r)*np.cos(np.radians(rad))*np.sin(np.radians(rad))
        y1=origin[1]+(ln+r)*np.sin(np.radians(rad))*np.sin(np.radians(rad))
        
        cv.delete("all")
        
        
        cv.create_line(origin[0],origin[1],origin[0]+x,origin[1]+y,
                    fill=color)
        draw_circle(x1,y1,r,color)
        
        if rad<=rad1:
            rad1=rad0
            rad+=radt
        
        elif rad>=rad1:
            rad1=180-rad0
            rad+=-1*radt
        
            
        root.after(30,draw_pendulum)   

         
                
        
        root.after(1,canvas_pendulum)
        
    return canvas_pendulum 
    

pend=draw_pendulum(500,30,"#ff0000")

pend()


root.mainloop()