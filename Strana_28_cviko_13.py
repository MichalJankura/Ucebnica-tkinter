import tkinter
canvas = tkinter.Canvas(width=550,height=150)
canvas.pack()
x=20
for i in range(1,11):
    canvas.create_line(20+x,50,50+x,80)
    canvas.create_line(50+x,50,20+x,80)
    x=x+30

x=20
for i in range(1,11):
    canvas.create_line(20+x,100,50+x,130)
    canvas.create_line(50+x,100,20+x,130)
    x=x+40

canvas.mainloop()
