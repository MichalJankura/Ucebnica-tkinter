import tkinter
canvas = tkinter.Canvas(width=800, height=800)
canvas.pack()

def button1_klik(poloha):
    x = poloha.x
    y = poloha.y
    farba = entry3.get()#Vstup pre farbu
    pocet = int(entry1.get())
    slovo = entry2.get()
    for i in range(pocet):
        canvas.create_text(x, y, text="            " + slovo, angle=i * 360 / pocet, fill=farba)

def zmaz():  # Vymazanie canvasu
    canvas.delete("all")

canvas.bind('<Button-1>', button1_klik)

entry1 = tkinter.Entry()  # Pole pre vstup počtu slov
entry1.pack()
entry2 = tkinter.Entry() # Pole pre vstup slova
entry2.pack()
entry3 = tkinter.Entry()  # Pole pre vstup farby
entry3.pack()

button_clear = tkinter.Button(text='Clear', command=zmaz)  # Tlačidlo pre vymazanie canvasu
button_clear.pack()

canvas.mainloop()