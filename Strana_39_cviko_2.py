import tkinter
canvas = tkinter.Canvas(width=450, height=450, bg="white")
canvas.pack()

def smajlik(suradnice):
    x = suradnice.x
    y = suradnice.y
    canvas.create_oval(x-20, y-20, x+20, y+20, width=2, fill="yellow")
    canvas.create_oval(x-10, y-10, x-5, y-5, width=2, fill="black")
    canvas.create_oval(x+5, y-10, x+10, y-5, width=2, fill="black")
    canvas.create_line(x-10, y+10, x+10, y+10, width=2, fill="black")



canvas.bind("<Button-1>", smajlik)
canvas.mainloop()