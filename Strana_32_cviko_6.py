import tkinter
canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()

def hrad(x,y):
    #BRANA
    canvas.create_rectangle(x,y+300,x+500,y+500)
    #STRIEŠKY
    canvas.create_line(x,y+300,x+50,y+100)
    canvas.create_line(x+50,y+100,x+100,y+300)

    canvas.create_line(x+450,y+100,x+500,y+300)
    canvas.create_line(x+400,y+300,x+450,y+100)
    #MURIVO
    for i in range(3):
        velkost = 80
        canvas.create_rectangle(x+150+(i*velkost),y+300,x+190+(i*velkost),y+260,fill="red")
    #OKNA
    canvas.create_oval(x+50,y+350,x+100,y+400,fill="blue")
    canvas.create_oval(x+450,y+350,x+400,y+400,fill="blue")

hrad(20,30)

canvas.mainloop()