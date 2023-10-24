import tkinter
from random import *
canvas = tkinter.Canvas(width=1920,height=1080)
canvas.pack()
def vagon(x, y):
    """Vagón"""
    canvas.create_rectangle(x, y, x+100, y+50,fill="green")

    """OKNÁ"""
    canvas.create_rectangle(x+5,y+10,x+50,y+30,fill="blue")
    canvas.create_rectangle(x+55,y+10,x+95,y+30,fill="blue")

    """SPOJ"""
    canvas.create_rectangle(x-20,y+40,x,y+30,fill="grey")

    """KOLESA"""
    canvas.create_oval(x, y+40,x+50,y+90,fill="black")
    canvas.create_oval(x+50, y+40,x+100,y+90,fill="black")

def rusen(x,y):

    """TELO"""
    canvas.create_rectangle(x,y+40,x+200,y-50,fill="green")
    canvas.create_rectangle(x+110,y-50,x+200,y-100,fill="red")
    canvas.create_rectangle(x+30,y-50,x+80,y-90,fill="blue")
    for i in range(0,6):
        posun = i*10
        canvas.create_line(x+30+posun,y-95,x+40+posun,y-120)

    """KOLESA"""
    canvas.create_oval(x, y+40,x+50,y+90,fill="black")
    canvas.create_oval(x+50, y+40,x+100,y+90,fill="black")
    canvas.create_oval(x+100, y+40,x+150,y+90,fill="black")
    canvas.create_oval(x+150, y+40,x+200,y+90,fill="black")

rusen(140,500)
for i in range(3,10):
    vagon(i*120, 500)

canvas.mainloop()
