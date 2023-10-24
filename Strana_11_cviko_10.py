import tkinter
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(10, 50, 110, 100,fill = "blue",outline="green",width=5)
canvas.create_rectangle(10, 100, 110, 150,fill = "red",outline="green",width=5)
canvas.create_rectangle(110, 50, 210, 100,fill = "yellow",outline="green",width=5)
canvas.create_rectangle(60, 75, 160, 125,fill = "brown",outline="green",width=5)

canvas.mainloop()
