import tkinter
from random import *
canvas = tkinter.Canvas(width=500, height=200)
canvas.pack()

def stvorcek(x, y, info):
    canvas.create_rectangle(x-10, y-10, x+10, y+10)
    canvas.create_text(x, y, text=info)

def button1_klik():
    od = int(entry1.get())
    do = int(entry2.get())
    base_x = 20  # Base x-coordinate representing the left edge of the screen
    for i in range (od, do):
        stvorcek(base_x + i*20, 100, i)  # Add i*20 to the base x-coordinate

button1 = tkinter.Button(text='postupnosť', command=button1_klik)
button1.pack()

entry1 = tkinter.Entry()
entry1.pack()

entry2 = tkinter.Entry()
entry2.pack()

canvas.mainloop()