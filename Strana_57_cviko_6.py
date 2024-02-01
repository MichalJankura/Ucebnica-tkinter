import tkinter
import random

canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()

def kresli_ciary(suradnice):
    pocet_ciar = int(entry1.get())
    medzera = int(entry2.get())
    dlzka_ciar = int(entry3.get())  # Get the length of the lines from the new entry widget

    colors = ["blue1", "blue2", "blue3", "blue4"]

    for i in range(pocet_ciar):
        x = suradnice.x + i * medzera + random.randint(-1, 1)
        color = random.choice(colors)
        canvas.create_line(x, suradnice.y - dlzka_ciar/2, x, suradnice.y + dlzka_ciar/2, fill=color)  # Use the length of the lines

def zmaz():
    canvas.delete("all")

entry1 = tkinter.Entry()  # Number of lines
entry1.pack()
entry2 = tkinter.Entry()  # Size of the gap
entry2.pack()
entry3 = tkinter.Entry()  # New entry widget for the length of the lines
entry3.pack()

button_clear = tkinter.Button(text='ZMAŽ', command=zmaz)
button_clear.pack()

canvas.bind("<Button-1>", kresli_ciary)

canvas.mainloop()