import tkinter
canvas = tkinter.Canvas(width=800, height=900,bg="white")
canvas.pack()

#ZMRZLINA-KOPČEKY
canvas.create_oval(380,300,580,100,fill="red",outline="")
canvas.create_oval(300,200,500,400,fill="yellow",outline="")
canvas.create_oval(450,200,650,400,fill="green",outline="")
#OBAL
canvas.create_rectangle(300,300,650,400,fill="white")
#KORNUT
canvas.create_line(300,400,475,800)
canvas.create_line(650,400,475,800)

canvas.mainloop()
