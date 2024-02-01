import tkinter
import random
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()

def kresli_ciary(suradnice):
    pocet_ciar = int(entry1.get())
    medzera = int(entry2.get())

    # Farby
    colors = ["blue1", "blue2", "blue3", "blue4"]

    # Kresli ciary
    for i in range(pocet_ciar):
        # Vyber nahodnu suradnicu x
        x = suradnice.x + i * medzera + random.randint(-1, 1)

        # Choose a random color
        color = random.choice(colors)

        # Draw the line
        canvas.create_line(x, suradnice.y - 50, x, suradnice.y + 50, fill=color)

def zmaz():
    canvas.delete("all")

entry1 = tkinter.Entry() # Pole pre vstup počtu čiar
entry1.pack()
entry2 = tkinter.Entry() # Pole pre vstup veľkosti medzery
entry2.pack()

# Tlačidlo pre vymazanie canvasu
button_clear = tkinter.Button(text='ZMAŽ', command=zmaz)
button_clear.pack()

canvas.bind("<Button-1>", kresli_ciary)

canvas.mainloop()