import tkinter
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_line(110, 10, 10, 200, 210, 200, 110, 10, fill='blue')
canvas.create_line(110, 200,310,200,210,10,110,200, fill='red')

canvas.mainloop()
