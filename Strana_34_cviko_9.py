import tkinter
import random
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()

def rebrik_1():
    canvas.create_line(50,40,300,600,fill="black")
    canvas.create_line(200,40,450,600,fill="black")
    for i in range(18):
        x1 = 10 + i * 15
        y1 = 50 + i * 30
        x2 = 250 + i * 15
        y2 = 50 + i * 30
        canvas.create_line(x1,y1,x2,y2,fill="black")



def rebrik_2():
    canvas.create_line(750, 40, 500, 600, fill="black")
    canvas.create_line(600, 40, 350, 600, fill="black")
    for i in range(18):
        x1 = 790 - i * 15
        y1 = 50 + i * 30
        x2 = 550 - i * 15
        y2 = 50 + i * 30
        canvas.create_line(x1, y1, x2, y2, fill="black")

rebrik_2()
#rebrik_1()
canvas.mainloop()