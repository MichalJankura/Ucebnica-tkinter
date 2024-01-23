import tkinter
from random import *

canvas = tkinter.Canvas(width=1000,height=650,bg="blue")
canvas.pack()

def kresli_rybuA(x,y,cislo):
    canvas.create_oval(x,y,x+35,y+15,fill='gold',width=2, tags='ryba')
    canvas.create_oval(x+10,y+3,x+15,y+8,fill='black', tags='ryba')
    canvas.create_line(x+35,y+7,x+45,y,x+45,y+15,x+35,y+7,width=2, tags='ryba')
    canvas.create_text(x+20,y-20,text=cislo,fill='white', tags="cislo")

def kresli_rybuB(x,y,cislo):
    canvas.create_oval(x,y,x-35,y+15,fill='gold',width=2, tags='ryba')
    canvas.create_oval(x-10,y+3,x-15,y+8,fill='black', tags='ryba')
    canvas.create_line(x-35,y+7,x-45,y,x-45,y+15,x-35,y+7,width=2, tags='ryba')
    canvas.create_text(x-20,y-20,text=cislo,fill='white',tags="cislo")

def klik(suradnice):
    x = suradnice.x
    y = suradnice.y
    global pocet_ryb
    maximum = int(entry1.get())
    if pocet_ryb<maximum and x<500:
        pocet_ryb = pocet_ryb+1
        kresli_rybuA(x,y,pocet_ryb)
        kresli_rybuB(1000-x,y,pocet_ryb)

def zmaz():
    global pocet_ryb
    canvas.delete("ryba", "cislo")
    pocet_ryb=0

pocet_ryb=0
canvas.create_line(500,0,500,650,width=5)
canvas.bind('<Button-1>',klik)
tlacidlo = tkinter.Button(text='Zmaž ryby',command=zmaz)
tlacidlo.pack()

entry1 = tkinter.Entry()
entry1.pack()

canvas.mainloop()
