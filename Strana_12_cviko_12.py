import tkinter
canvas = tkinter.Canvas(width=300, height=200)
canvas.pack()

canvas.create_rectangle(0,0,300,200,fill = "red")
canvas.create_rectangle(0,70,300,130,fill="white")

canvas.mainloop()
