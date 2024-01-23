import tkinter
import math
import os
from random import *

canvas = tkinter.Canvas(height=400, width=1000)
canvas.pack()

#---------TUTORIAL---------
canvas.create_text(500,80,text='Nápoveda:',tags='instrukcie')
canvas.create_text(500,95,text='Ovládate modrý tank šípkami',tags='instrukcie')
canvas.create_text(500,110,text='Nastavte mu počiatočnú rýchlosť výstrelu a uhol, pod ktorým má vystreliť',tags='instrukcie')
canvas.create_text(500,125,text='Po stlačení tlačidla "výstrel" sa vaša strela dopraví k červenému tanku',tags='instrukcie')
canvas.create_text(500,140,text='Ak ho zasiahnete, vyhrali ste, ak nie, na ťahu je počítač',tags='instrukcie')
canvas.create_text(500,155,text='Akonáhle niekto vyhrá, program sa sám vypne',tags='instrukcie')
canvas.create_text(500,170,text='Pre skrytie nápovedy stlačte medzerník',tags='instrukcie')

def zmaz(event):
    canvas.delete('instrukcie')

canvas.bind_all('<space>', zmaz)


canvas.create_line(0,250,1000,250)

entry1 = tkinter.Entry()
entry1.pack()
entry1.insert(0, 'Zadajte rychlost(m/s)')

entry2 = tkinter.Entry()
entry2.pack()
entry2.insert(0, 'Zadajte uhol(°)')


hrac_x = 50
hrac_y = 240
canvas.create_rectangle(hrac_x-10,hrac_y, hrac_x+10,hrac_y+10, fill='grey', tags='hrac')
canvas.create_oval(hrac_x-20, hrac_y, hrac_x+20, hrac_y+10, fill='grey', tags='hrac')
canvas.create_rectangle(hrac_x-8, hrac_y-8, hrac_x+8, hrac_y, fill='blue', tags='hrac')
canvas.create_line(hrac_x+8,hrac_y-5,hrac_x+20,hrac_y-10, width=3, tags='hrac')


pocitac_x = 950
pocitac_y = 240
canvas.create_rectangle(pocitac_x-10,pocitac_y, pocitac_x+10, pocitac_y+10, fill='grey', tags='pocitac')
canvas.create_oval(pocitac_x-20, pocitac_y, pocitac_x+20, pocitac_y+10, fill='grey', tags='pocitac')
canvas.create_rectangle(pocitac_x-8, pocitac_y-8, pocitac_x+8, pocitac_y, fill='red', tags='pocitac')
canvas.create_line(pocitac_x-8,pocitac_y-5,pocitac_x-20,pocitac_y-10, width=3, tags='pocitac')

palivo = 120
canvas.create_rectangle(20,40,palivo,60, fill='black', tags='palivo')
canvas.create_text(70,20, text='Palivo:')

obtiaznost = 100

def pohyb_hrac_right(event):
    global hrac_x, palivo
    if hrac_x<1000 and palivo>20:
        canvas.move('hrac', 5, 0)
        hrac_x = hrac_x+5
        palivo = palivo-5
        canvas.delete('palivo')
        canvas.create_rectangle(20,40,palivo,60, fill='black', tags='palivo')
        
        
canvas.bind_all('<Right>', pohyb_hrac_right)

def pohyb_hrac_left(event):
    global hrac_x, palivo
    if hrac_x>0 and palivo>20:
        canvas.move('hrac', -5, 0)
        hrac_x = hrac_x-5
        palivo = palivo-5
        canvas.delete('palivo')
        canvas.create_rectangle(20,40,palivo,60, fill='black', tags='palivo')

canvas.bind_all('<Left>', pohyb_hrac_left)

def vystrel():
    global palivo, obtiaznost
    canvas.delete('vystrel')
    v = float(entry1.get())
    uhol = float(entry2.get())
    radian = math.radians(uhol)
    dostrel = v*v/10*math.sin(2*radian)
    miesto_dopadu = hrac_x+dostrel
    x = hrac_x
    for i in range(1,10):
        x = x+dostrel/18
        y = 240-2*uhol*math.sin(math.radians(i*10))
        canvas.create_oval(x-3,y-3,x+3,y+3, fill='black',tags='vystrel')
        canvas.update()
        canvas.after(50)
    for i in range(10,19):
        x = x+dostrel/18
        y = 240-2*uhol*math.sin(math.radians(i*10))
        canvas.create_oval(x-3,y-3,x+3,y+3, fill='black',tags='vystrel')
        canvas.update()
        canvas.after(50)
    canvas.create_oval(miesto_dopadu-10,230,miesto_dopadu+10,250, fill='blue', tags='vystrel')
    if pocitac_x-20 <= miesto_dopadu <= pocitac_x+20:
        canvas.create_text(500,100, text='Vyhrali ste', font='Arial 50 bold')
        canvas.update()
        canvas.after(5000)
        os._exit(0)
    palivo = 10
    canvas.update()
    canvas.after(3000)
    canvas.delete('vystrel')
    dostrel_pocitac = pocitac_x-hrac_x+randrange(-obtiaznost, obtiaznost)
    miesto_dopadu_pocitac = pocitac_x-dostrel_pocitac
    x = pocitac_x
    for i in range(1,10):
        x = x-dostrel_pocitac/18
        y = 240-200*math.sin(math.radians(i*10))
        canvas.create_oval(x-3,y-3,x+3,y+3, fill='black',tags='vystrel')
        canvas.update()
        canvas.after(50)
    for i in range(10,19):
        x = x-dostrel_pocitac/18
        y = 240-200*math.sin(math.radians(i*10))
        canvas.create_oval(x-3,y-3,x+3,y+3, fill='black',tags='vystrel')
        canvas.update()
        canvas.after(50)
    canvas.create_oval(miesto_dopadu_pocitac-10,230,miesto_dopadu_pocitac+10,250, fill='red', tags='vystrel')
    if hrac_x-20 <= miesto_dopadu_pocitac <= hrac_x+20:
        canvas.create_text(500,100, text='Vyhral pocitac')
        canvas.update()
        canvas.after(5000)
        os._exit(0)
    obtiaznost = obtiaznost-5
    palivo = 120
    canvas.delete('palivo')
    canvas.create_rectangle(20,40,palivo,60, fill='black', tags='palivo')    


button1 = tkinter.Button(text='vystrel', command=vystrel)
button1.pack()

canvas.mainloop()

#vyhra - 103,60
