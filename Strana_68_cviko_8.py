import tkinter
from random import *

canvas = tkinter.Canvas(height=300, width=500)
canvas.pack()

def bosorka_vlavo(canvas, x_1, y_1):
    # hlava s telom
    canvas.create_oval(x_1 - 10, y_1 - 40, x_1 + 10, y_1 - 20)
    canvas.create_rectangle(x_1 - 10, y_1 - 20, x_1 + 10, y_1 + 20)
    # metla
    canvas.create_line(x_1 - 30, y_1, x_1 + 30, y_1)
    canvas.create_line(x_1 - 30, y_1, x_1 - 60, y_1)
    canvas.create_line(x_1 - 30, y_1, x_1 - 60, y_1 - 10)
    canvas.create_line(x_1 - 30, y_1, x_1 - 60, y_1 - 20)
    canvas.create_line(x_1 - 30, y_1, x_1 - 60, y_1 - 30)
    canvas.create_line(x_1 - 30, y_1, x_1 - 60, y_1 - 40)
    canvas.create_line(x_1 - 30, y_1, x_1 - 60, y_1 + 10)
    canvas.create_line(x_1 - 30, y_1, x_1 - 60, y_1 + 20)
    canvas.create_line(x_1 - 30, y_1, x_1 - 60, y_1 + 30)
    canvas.create_line(x_1 - 30, y_1, x_1 - 60, y_1 + 40)

def bosorka_vpravo(canvas, x_2, y_2):
    # hlava s telom
    canvas.create_oval(x_2 - 10, y_2 - 40, x_2 + 10, y_2 - 20)
    canvas.create_rectangle(x_2 - 10, y_2 - 20, x_2 + 10, y_2 + 20)
    # metla
    canvas.create_line(x_2 - 30, y_2, x_2 + 30, y_2)
    canvas.create_line(x_2 - 30, y_2, x_2 - 60, y_2)
    canvas.create_line(x_2 - 30, y_2, x_2 - 60, y_2 - 10)
    canvas.create_line(x_2 - 30, y_2, x_2 - 60, y_2 - 20)
    canvas.create_line(x_2 - 30, y_2, x_2 - 60, y_2 - 30)
    canvas.create_line(x_2 - 30, y_2, x_2 - 60, y_2 - 40)
    canvas.create_line(x_2 - 30, y_2, x_2 - 60, y_2 + 10)
    canvas.create_line(x_2 - 30, y_2, x_2 - 60, y_2 + 20)
    canvas.create_line(x_2 - 30, y_2, x_2 - 60, y_2 + 30)
    canvas.create_line(x_2 - 30, y_2, x_2 - 60, y_2 + 40)

x_1 = 150
y_1 = 60

x_2 = 350
y_2 = 60

bosorka_vlavo(canvas, x_1, y_1)
bosorka_vpravo(canvas, x_2, y_2)

def timer():
    global x_1, y_1, x_2, y_2
    cislo1 = choice(('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))
    cislo2 = choice(('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))
    y_1 = y_1 + int(cislo1)
    y_2 = y_2 + int(cislo2)
    canvas.delete('all')
    bosorka_vlavo(canvas, x_1, y_1)
    bosorka_vpravo(canvas, x_2, y_2)
    if y_1 >= 300:
        canvas.create_text(250, 150, text='Vyhrala bosorka vlavo')
    elif y_2 >= 300:
        canvas.create_text(250, 150, text='Vyhrala bosorka vpravo')
    else:
        canvas.after(100, timer)

timer()
canvas.mainloop()
