import tkinter
from random import *
canvas = tkinter.Canvas()
canvas.pack()
def kresli_lopticku(x, y):
    canvas.create_oval(x-5, y-5,x+5, y+5, fill='red')
def kresli_kurzor(x, y):
    canvas.create_line(x, y, x+50, y, fill='blue', width=5)
def vypis_body(pocet_bodov):
    canvas.create_text(100, 10, text='Počet získaných bodov:')
    canvas.create_text(200, 10, text=pocet_bodov)
def timer1():
    canvas.delete('all')
    global lopticka_x, lopticka_y, pocet_bodov
    lopticka_y = lopticka_y + 5
    kresli_lopticku(lopticka_x, lopticka_y)
    kresli_kurzor(kurzor_x, kurzor_y)
    vypis_body(pocet_bodov)
    if kurzor_x<lopticka_x<kurzor_x+50 and kurzor_y-10<lopticka_y<kurzor_y:
        pocet_bodov = pocet_bodov + 1
        lopticka_x = randrange(300)
        lopticka_y = 20
    elif lopticka_y>300:
        pocet_bodov = pocet_bodov - 1  # Subtract a point if the ball has reached the bottom
        lopticka_x = randrange(300)
        lopticka_y = 20
    canvas.after(10, timer1)
def posun_mysi(suradnice):
    global pocet_bodov, kurzor_x
    kurzor_x = suradnice.x
    canvas.delete('all')
    kresli_lopticku(lopticka_x, lopticka_y)
    kresli_kurzor(kurzor_x, kurzor_y)
    vypis_body(pocet_bodov)

pocet_bodov = 0
lopticka_x = randrange(300)
lopticka_y = 20
kurzor_x = 150
kurzor_y = 250

timer1()
canvas.bind('<Motion>', posun_mysi)

canvas.mainloop()