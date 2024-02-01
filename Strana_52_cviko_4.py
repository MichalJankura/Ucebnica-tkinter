"""KLIKNEŠ A ZASTAVÍ SA LOPTIČKA"""
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
        canvas.after(100, lopticka)
def stop(suradnice):
    global pokracovat
    pokracovat = 0

pokracovat = 1
x = 200
y = 5
lopticka()
canvas.bind('<Button-1>',stop)
canvas.mainloop()