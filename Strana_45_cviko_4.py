import tkinter
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()

def draw_flag(suradnice):
    # FARBY NEMECKA
    colors = ["black", "red", "gold"]
    for i in range(3):
        y1 = suradnice.y + i * 20
        y2 = y1 + 20
        canvas.create_rectangle(suradnice.x, y1, suradnice.x + 60, y2, fill=colors[i], outline="")

canvas.bind("<Button-1>", draw_flag)
canvas.mainloop()