import tkinter
canvas = tkinter.Canvas(width=600,height=600,background="white")
canvas.pack()


def postava(x,y):
    #ŠATY
    canvas.create_line(x,y+400,x+100,y+400,fill="black")
    canvas.create_line(x,y+400,x+50,y+200,fill="black")
    canvas.create_line(x+50,y+200,x+100,y+400,fill="black")
    #NOHY
    canvas.create_rectangle(x+30,y+400,x+40,y+430,fill="red")
    canvas.create_rectangle(x+60,y+400,x+70,y+430,fill="red")
    #HLAVA
    canvas.create_oval(x+30,y+160,x+70,y+200,fill="red")

postava(90,20)

canvas.mainloop()