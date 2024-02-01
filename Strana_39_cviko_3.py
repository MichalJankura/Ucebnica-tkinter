import tkinter
canvas = tkinter.Canvas(width=450, height=450, bg="white")
canvas.pack()

def trava(suradnice):
    x = suradnice.x
    y = suradnice.y
    canvas.create_line(x, y, 225, 450, width=5, fill="green")

canvas.bind("<Button-1>", trava)
canvas.mainloop()