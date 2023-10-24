import tkinter
canvas = tkinter.Canvas(bg = 'white', width = 300, height = 200)
canvas.pack()

canvas.create_rectangle(0, 0, 300, 200, fill="white",outline="")
canvas.create_oval(100, 50, 200, 150, fill="red",outline="")

canvas.mainloop()
