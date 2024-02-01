import tkinter
canvas = tkinter.Canvas(width=450, height=450, bg="white")
canvas.pack()

def krizik(suradnice):
    x = suradnice.x
    y = suradnice.y
    canvas.create_line(x-10, y-10, x+10, y+10, width=2, fill="red")
    canvas.create_line(x-10, y+10, x+10, y-10, width=2, fill="red")

canvas.bind("<Button-1>", krizik)
canvas.mainloop()