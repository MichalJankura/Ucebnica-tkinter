import tkinter
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()

def kresli_znacku(suradnice):
    nazov_mesta = entry1.get()
    typ_znacky = entry2.get()

    # obrys obdlznika pre znacku
    x1, y1 = suradnice.x - 50, suradnice.y - 20
    x2, y2 = suradnice.x + 50, suradnice.y + 20
    canvas.create_rectangle(x1, y1, x2, y2)

    # Názov mesta výpis do stredu obdlznika
    canvas.create_text(suradnice.x, suradnice.y, text=nazov_mesta)

    # ak je typ znacky "k" tak sa vykresli znacka koniec
    if typ_znacky.lower() == 'k':
        canvas.create_line(x1, y1, x2, y2)

    # Tyčka
    dlzka_tyce = 100
    canvas.create_line(suradnice.x, y2, suradnice.x, y2 + dlzka_tyce)

def zmaz():
    canvas.delete("all")

# Inicializacia premennych pre vstupy
entry1 = tkinter.Entry() # Názov mesta
entry1.pack()
entry2 = tkinter.Entry() # Typ dopravnej značky ak "k" tak koniec
entry2.pack()

# Tlačidlo pre vymazanie canvasu
button_clear = tkinter.Button(text='ZMAŽ', command=zmaz)
button_clear.pack()

canvas.bind("<Button-1>", kresli_znacku)

canvas.mainloop()