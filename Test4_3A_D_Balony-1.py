import tkinter
from random import *
canvas = tkinter.Canvas(width=1000,height=600)
canvas.pack()

def klik_lavy(suradnice):
    x=suradnice.x
    farba_lavy=entry1.get()
    canvas.create_oval(x-10,540,x+10,560,fill=farba_lavy,tags='balon_lavy')

def klik_pravy(suradnice):
    x=suradnice.x
    farba_pravy=entry2.get()
    canvas.create_oval(x-10,540,x+10,560,fill=farba_pravy,tags='balon_pravy')
   
def animuj():
    global vyska_lavy, vyska_pravy
    posun_lavy=randint(1,30)
    posun_pravy=randint(1,30)
    canvas.move('balon_lavy',0,-posun_lavy)
    canvas.move('balon_pravy',0,-posun_pravy)
    vyska_lavy=vyska_lavy-posun_lavy
    vyska_pravy=vyska_pravy-posun_pravy
    if vyska_pravy<0 and vyska_pravy<vyska_lavy:
        canvas.create_text(500,300,text='Vyhral pravý balón!', font="Arial 25")
    elif vyska_lavy<0 and vyska_lavy<vyska_pravy:
        canvas.create_text(500,300,text='Vyhral ľavý balón!', font="Arial 25")
    else:
        canvas.after(100,animuj)



vyska_lavy=550
vyska_pravy=550
canvas.bind('<Button-1>',klik_lavy)
canvas.bind('<Button-3>',klik_pravy)
button1=tkinter.Button(text='Vypusť balóny',command=animuj)
button1.pack()
entry1=tkinter.Entry()
entry1.pack()
entry2=tkinter.Entry()
entry2.pack()

canvas.mainloop()
