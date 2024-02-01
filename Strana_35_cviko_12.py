import tkinter
canvas = tkinter.Canvas(width=450, height=450, bg="white")
canvas.pack()

for i in range(10):
    start = 50 * i
    # Vertikalne čiary
    canvas.create_line(start, 0, start, 450, width=2)
    # Horizontalne čiary
    canvas.create_line(0, start, 450, start, width=2)

canvas.mainloop()