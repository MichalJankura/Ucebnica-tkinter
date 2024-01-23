import tkinter
from random import *
canvas = tkinter.Canvas()
canvas.pack()

def timer1():
    canvas.delete('all')
    global sx, sy
    sx = randrange(300)
    sy = randint(20, 250)
    canvas.create_rectangle(sx, sy, sx+velkost, sy+velkost, fill='green')
    canvas.create_text(100, 10, text='Počet získaných bodov:')
    canvas.create_text(200, 10, text=pocet_bodov)
    if -10<pocet_bodov<10:
        canvas.after(1000, timer1)
    elif pocet_bodov==10:
        print("Si super!")

    else:
       print("Naprav sa!") 

def klik(suradnice):
    global pocet_bodov
    x = suradnice.x
    y = suradnice.y
    if sx < x < sx+velkost and sy < y < sy+velkost:
        pocet_bodov = pocet_bodov + 1
    else:
        pocet_bodov = pocet_bodov - 1
    

pocet_bodov = 0

velkost = 50
timer1()
canvas.bind('<Button-1>', klik)

canvas.mainloop()
