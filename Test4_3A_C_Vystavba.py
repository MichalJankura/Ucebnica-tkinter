import tkinter
from random import *
canvas = tkinter.Canvas(width=1000,height=600)
canvas.pack()

def klik(suradnice):
    global vyska
    x=suradnice.x
    vyska=int(entry1.get())
    farba=choice(('blue','red','green'))
    canvas.create_rectangle(x,600-vyska,x+100,600,fill=farba,tags='panelak')
   
def animuj():
    global vystavba
    if vystavba==0:
        canvas.move('panelak',0,vyska)
    canvas.move('panelak',0,-5)
    vystavba=vystavba+5
    if vystavba<=vyska:
        canvas.after(100,animuj)

def zmaz():
    global vystavba
    canvas.delete('all')
    vystavba=0

vystavba=0
canvas.bind('<Button-1>',klik)
button1=tkinter.Button(text='spusti výstavbu',command=animuj)
button1.pack()
button2=tkinter.Button(text='zmaž',command=zmaz)
button2.pack()
entry1=tkinter.Entry()
entry1.pack()

canvas.mainloop()
