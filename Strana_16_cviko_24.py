import tkinter
canvas = tkinter.Canvas(width = 800, height = 600)
canvas.pack()

#HOSPITAL
canvas.create_rectangle(0,0,250,250,fill="blue")
canvas.create_text(130,110,text="H",font= "Arial 140 bold",fill="white")
canvas.create_text(125,220,text="NEMOCNICA",font= "Arial 25 bold",fill="white")

#POLICE
canvas.create_rectangle(260,0,410,250,fill="blue")
canvas.create_rectangle(280,20,390,140,fill="white",outline="")
canvas.create_text(335,75,text="Polícia",font= "Arial 25 bold",fill="black")

#80-Warning
canvas.create_oval(420,10,660,250,fill="white")
canvas.create_oval(430,20,650,240,fill="red",outline="")
canvas.create_oval(460,50,620,210,fill="white",outline="")
canvas.create_text(540,130,text="80",font= "Arial 80 bold",fill="black")

#P RÉSERVÉ
canvas.create_rectangle(0,260,160,510,fill="blue")
canvas.create_text(80,490,text="RÉSERVÉ",font= "Arial 25 bold",fill="white")
canvas.create_text(80,360,text="P",font= "Arial 150 bold",fill="white")

#6t
canvas.create_oval(170,260,420,510,fill="red")
canvas.create_oval(200,290,390,480,fill="white",outline="")
canvas.create_text(290,380,text="6 t",font= "Arial 80 bold",fill="black")

canvas.mainloop()
