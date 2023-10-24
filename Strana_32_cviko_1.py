import tkinter
from random import *
canvas = tkinter.Canvas(width=1300,height=250)
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

for i in range(1, 7):
    vagon(i*120, 100)


canvas.mainloop()
