import tkinter
from random import *
canvas = tkinter.Canvas(width=1000,height=650)
canvas.pack()

def klik(suradnice):
    x = 500
    y = suradnice.y
    canvas.create_text(x,y,text=entry1.get(), font='Arial 30',tags='titulky')

def pusti():
    global pozicia_y
    canvas.move('titulky',0,-10)
    pozicia_y=pozicia_y-10
    if pozicia_y<-100:
        pozicia_y=1000
        canvas.move('titulky',0,1100)
    canvas.after(100,pusti)

def start():
    canvas.move('titulky',0,600)
    pusti()

def zmaz():
    canvas.delete('all')

pozicia_y=1000
entry1 = tkinter.Entry()
entry1.pack()
button1 = tkinter.Button(text='Pusti titulky',command=start)
button1.pack()
button2 = tkinter.Button(text='Zmaž',command=zmaz)
button2.pack()
canvas.bind('<Button-1>',klik)
