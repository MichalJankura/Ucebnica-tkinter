import tkinter
canvas = tkinter.Canvas(width=400,height=400)
canvas.pack()

for i in range(10, 16):
    y = 20*i
    canvas.create_rectangle(100, y, 200, y+10)

canvas.mainloop()
