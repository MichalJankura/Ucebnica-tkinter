import tkinter
from random import *
canvas = tkinter.Canvas(width=1000,height=600,bg="blue")
canvas.pack()

def kresli_hviezduA(x,y,cislo):
    canvas.create_line(x,y,x+10,y+10, fill="gold", tags="hviezda")
    canvas.create_line(x+10,y,x,y+10, fill="gold", tags="hviezda")
    canvas.create_text(x+5,y-5,text=cislo,fill='white', tags="cislo")

def kresli_hviezduB(x,y,cislo):
    canvas.create_line(x,y,x+10,y+10, fill="gold", tags="hviezda")
    canvas.create_line(x+10,y,x,y+10, fill="gold", tags="hviezda")
    canvas.create_text(x+5,y-5,text=cislo,fill='white', tags="cislo")    


def klik(suradnice):
    x = suradnice.x
    y = suradnice.y
    global pocet_hviezd
    maximum = int(entry1.get())
    if pocet_hviezd<maximum and y<300:
        pocet_hviezd = pocet_hviezd+1
        kresli_hviezduA(x,y,pocet_hviezd)
        kresli_hviezduB(x,600-y,pocet_hviezd)

def zmaz():
    global pocet_hviezd
    canvas.delete("hviezda", "cislo")
    pocet_hviezd=0

pocet_hviezd=0
canvas.bind('<Button-1>',klik)
tlacidlo = tkinter.Button(text='Zmaž hviezdy',command=zmaz)
tlacidlo.pack()
entry1 = tkinter.Entry()
entry1.pack()


def posun_vlavo(event):
    canvas.move('all',5,0)
canvas.bind_all('<Left>',posun_vlavo)


canvas.create_rectangle(-1000,0,10000,300,fill="black")
canvas.create_rectangle(-1000,300,10000,600,fill="blue")

canvas.mainloop()
