import tkinter
canvas = tkinter.Canvas(bg = 'white', width = 250, height = 200)
canvas.pack()

canvas.create_oval(10,10,160,160,fill = "red",outline="")
canvas.create_oval(40,20,190,150,fill = "white",outline="")

canvas.mainloop()
