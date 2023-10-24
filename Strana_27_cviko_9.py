import tkinter
canvas = tkinter.Canvas(width=800,height=400)
canvas.pack()

"""From left to the right"""
x,y = 50,50
for i in range(5):
    canvas.create_line(x,y,x+50,y)
    canvas.create_line(x+50,y,x+50,y+50)
    x = x+50
    y = y+50

x2,y2 = 700,50

"""From right to the left"""
for i in range(5):
    canvas.create_line(x2,y2,x2-50,y2)
    canvas.create_line(x2-50,y2,x2-50,y2+50)
    x2 = x2-50
    y2 = y2+50

canvas.mainloop()
