import tkinter
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_line(110,10,210,10,width = 2)
canvas.create_line(110,10,110,60,width = 2)
canvas.create_line(210,10,210,60,width = 2)
canvas.create_line(110,60,210,60,width = 2)

canvas.mainloop()
