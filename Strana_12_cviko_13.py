import tkinter
canvas = tkinter.Canvas(width=300, height=200)
canvas.pack()

#BELOTA
canvas.create_rectangle(0,0,300,200,fill="white")

#VRCHNY STVOREC
canvas.create_rectangle(0,0,40,40,fill = "blue",outline="")
canvas.create_rectangle(0,60,40,100,fill = "blue",outline="")
canvas.create_rectangle(60,0,100,40,fill = "blue",outline="")
canvas.create_rectangle(60,60,100,100,fill = "blue",outline="")
#----------------------------------------------------

#PASY PO DRUHY STVOREC
canvas.create_rectangle(100,0,300,20,fill = "blue",outline="")
canvas.create_rectangle(100,40,300,60,fill = "blue",outline="")
canvas.create_rectangle(100,80,300,100,fill = "blue",outline="")

#DOLNE DVA PASY
canvas.create_rectangle(0,120,300,140,fill = "blue",outline="")
canvas.create_rectangle(0,160,300,180,fill = "blue",outline="")

canvas.mainloop()
