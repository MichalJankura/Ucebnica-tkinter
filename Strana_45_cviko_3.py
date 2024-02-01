import tkinter

canvas = tkinter.Canvas(width=400, height=400, bg="white")
canvas.pack()

def ciary(suradnice):
    x = suradnice.x
    y = suradnice.y
    if x < 200:
        if y < 200:
            canvas.create_line(x, y, 200, 200, fill='red', width=5)
        else:
            canvas.create_line(x, y, 200, 200, fill='blue', width=5)
    else:
        if y < 200:
            canvas.create_line(x, y, 200, 200, fill='green', width=5)
        else:
            canvas.create_line(x, y, 200, 200, fill='yellow', width=5)


canvas.bind('<Button-1>', ciary)
canvas.mainloop()