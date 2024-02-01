import tkinter
from random import *
canvas = tkinter.Canvas()
canvas.pack()

def timer1():
    canvas.delete('all')
    global sx, sy, velkost
    sx = randrange(300)
    sy = randint(20, 250)
    if random() < 0.5:  # 50% šanca na vykreslenie zeleného obdĺžnika
        canvas.create_rectangle(sx, sy, sx+velkost, sy+velkost, fill='green')
    else:  # 50% šanca na vykreslenie červeného obdĺžnika
        canvas.create_rectangle(sx, sy, sx+velkost, sy+velkost, fill='red')
    canvas.create_text(100, 10, text='Počet získaných bodov:')
    canvas.create_text(200, 10, text=pocet_bodov)
    if pocet_bodov < -10:
        print("Zlepši sa")
        return
    canvas.after(500, timer1)

def klik(suradnice):
    global pocet_bodov
    x = suradnice.x
    y = suradnice.y
    if sx < x < sx+velkost and sy < y < sy+velkost:
        color = canvas.itemcget(canvas.find_closest(x, y), "fill")  # zisti farbu kliknutého obdĺžnika
        if color == "green":
            pocet_bodov = pocet_bodov + 1
        elif color == "red":
            pocet_bodov = pocet_bodov - 2
            if pocet_bodov < -10:
                print("Zlepši sa")

pocet_bodov = 0
sx = 0
sy = 0
velkost = 50
timer1()
canvas.bind('<Button-1>', klik)
canvas.mainloop()