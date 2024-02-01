import tkinter
from random import *

canvas = tkinter.Canvas(width=800, height=800)
canvas.pack()


def button1_klik(poloha):
    x = poloha.x
    y = poloha.y
    farba = choice(("red", "blue", "green", "yellow"))
    pocet = int(entry1.get())
    slovo = entry2.get()
    for i in range(pocet):
        canvas.create_text(x, y, text="            " + slovo, angle=i * 360 / pocet, fill=farba)


canvas.bind('<Button-1>', button1_klik)

entry1 = tkinter.Entry()
entry1.pack()
entry2 = tkinter.Entry()
entry2.pack()

canvas.mainloop()