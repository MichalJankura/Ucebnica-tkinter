import tkinter
import random
canvas = tkinter.Canvas(width=1000, height=500, bg="white")
canvas.pack()

def obrazok_1():
    stred_x = 500
    stred_y = 500
    for i in range(100):
        x1 = 10*i
        y1 = 0
        canvas.create_line(stred_x, stred_y, x1, y1, fill="black")

def obrazok_2():
    roh_x = 0
    roh_y = 0
    for i in range(100):
        x1 = 10*i
        y1 = 500
        canvas.create_line(roh_x, roh_y, x1, y1, fill="green")

def obrazok_3():
    roh_x = 1000
    roh_y = 500
    for i in range(100):
        x1 = 10*i
        y1 = 0
        canvas.create_line(roh_x, roh_y, x1, y1, fill="blue")


#obrazok_1()
#obrazok_2()
obrazok_3()
canvas.mainloop()