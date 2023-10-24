import tkinter
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_line(20,20,250,250,fill = "blue",width = 50)
canvas.create_line(20,20,250,250,fill = "yellow",width = 40)
canvas.create_line(20,20,250,250,fill = "green",width = 30)
canvas.create_line(20,20,250,250,fill = "blue",width = 20)
canvas.create_line(20,20,250,250,fill = "white",width = 10)
canvas.create_line(20,20,250,250,fill = "black",width = 5)

canvas.mainloop()
