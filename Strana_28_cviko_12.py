import tkinter
canvas = tkinter.Canvas(background="black",width=1000,height=800)
canvas.pack()

x=10
y=10
for i in range(1,26):
    x=x+20
    y=y+20
    canvas.create_line(x,10,510,y,fill='white',width=2)
    canvas.update()
    canvas.after(100)
############################################################
x=530
y=530
for i in range(1,26):
    x=x-20
    y=y-20
    canvas.create_line(x,510,10,y,fill='white',width=2)
    canvas.update()
    canvas.after(100)
############################################################

x=530
y=10
for i in range(1,26):
    x=x-20
    y=y+20
    canvas.create_line(x,10,10,y,fill='white',width=2)
    canvas.update()
    canvas.after(100)
############################################################
x=10
y=530
for i in range(1,26):
    x=x+20
    y=y-20
    canvas.create_line(x,500,500,y,fill='white',width=2)
    canvas.update()
    canvas.after(100)

canvas.mainloop()
