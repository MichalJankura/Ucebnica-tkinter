"""KLIKNEŠ A ZASTAVÍ SA , KLIKNEŠ ZNOVA A SPUSTI SA LOPTIČKA"""
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def lopticka():
    global y
    canvas.delete('all')
    canvas.create_oval(x-5, y-5, x+5, y+5)
    y = y+5
    if y>250:
        y = 5
    if pokracovat == 1:
        canvas.after(10, lopticka)

def stop(suradnice):
    global pokracovat
    if pokracovat == 1:
        pokracovat = 0
    else:
        pokracovat = 1
        lopticka()

pokracovat = 1
x = 200
y = 5
lopticka()
canvas.bind('<Button-1>',stop)
canvas.mainloop()