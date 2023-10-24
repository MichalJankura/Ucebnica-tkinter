import tkinter
canvas = tkinter.Canvas(bg = 'white', width = 250, height = 600)
canvas.pack()

#BODY
canvas.create_rectangle(50,400,200,600,fill="green")
#FACE
canvas.create_oval(50,250,200,400,fill="#f0e171")
#EYES
canvas.create_oval(100,300,110,310,fill="black")
canvas.create_oval(150,300,160,310,fill="black")
#LIPS
canvas.create_line(125,350,165,350,width=2)
#HAT
canvas.create_oval(40,240,210,280,fill="black")
canvas.create_rectangle(60,140,190,250,fill="black")
canvas.create_oval(60,120,190,160,fill="black")
canvas.mainloop()
