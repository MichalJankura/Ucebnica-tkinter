import tkinter
from random import *
canvas = tkinter.Canvas()
canvas.pack()

def timer1():
    canvas.delete('all')
    global sx, sy, velkost
    sx = randrange(300)
    sy = randint(20, 250)
    if random() < 0.5 + pocet_bodov * 0.01:  # Zvýš šancu na vykreslenie zeleného obdĺžnika
        canvas.create_rectangle(sx, sy, sx+velkost, sy+velkost, fill='red')
    else:
        canvas.create_rectangle(sx, sy, sx+velkost, sy+velkost, fill='green')
    canvas.create_text(100, 10, text='Počet získaných bodov:')
    canvas.create_text(200, 10, text=pocet_bodov)
    if pocet_bodov > 10:
        print("Gratulujem k výborným reakciám!")
        return
    if pocet_bodov < -10:
        print("Zlepši sa")
        return
    delay = max(500 - pocet_bodov * 5, 40)  # Increase the delay to make the animation slower
    canvas.after(delay, timer1)

def klik(suradnice):
    global pocet_bodov, velkost
    x = suradnice.x
    y = suradnice.y
    if sx < x < sx+velkost and sy < y < sy+velkost:
        color = canvas.itemcget(canvas.find_closest(x, y), "fill")  # Zisti farbu kliknutého obdĺžnika
        if color == "green":
            pocet_bodov = pocet_bodov + 1
            velkost = max(10, velkost - 2)  # Zmenšuj veľkosť štvorca
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