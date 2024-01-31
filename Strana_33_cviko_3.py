import tkinter
canvas = tkinter.Canvas(width=800, height=900)
canvas.pack()

def ballon_with_basket(x, y):
    canvas.create_oval(x + 50, y + 50, x + 250, y + 250, fill="blue")
    canvas.create_line(x+50,y+170,x+90,y+500)


ballon_with_basket(400,250)
canvas.mainloop()
