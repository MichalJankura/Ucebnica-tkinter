import tkinter
canvas = tkinter.Canvas(bg = 'white', width = 250, height = 250)
canvas.pack()

canvas.create_oval(10,10,240,240,fill="red")
canvas.create_oval(20,20,230,230,fill="green")
canvas.create_oval(30,30,220,220,fill="blue")
canvas.create_oval(40,40,210,210,fill="yellow")
canvas.create_oval(50,50,200,200,fill="pink")
canvas.create_oval(60,60,190,190,fill="orange")
canvas.create_oval(70,70,180,180,fill="purple")
canvas.create_oval(80,80,170,170,fill="navyblue")
canvas.create_oval(90,90,160,160,fill="grey")
canvas.create_oval(100,100,150,150,fill="brown")
canvas.create_oval(110,110,140,140,fill="red")

canvas.create_line(125,10,125,240,width=2)
canvas.create_line(10,125,240,125,width=2)

canvas.mainloop()
