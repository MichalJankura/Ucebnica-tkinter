import tkinter
canvas = tkinter.Canvas(width = 800, height = 600)
canvas.pack()

#80_01
canvas.create_oval(10,10,250,250,fill="white")
canvas.create_oval(20,20,240,240,fill="red",outline="")
canvas.create_oval(50,50,210,210,fill="white",outline="")
canvas.create_text(130,130,text="80",font= "Arial 80 bold",fill="black")
#Warning_sign_01 "22:00 - 06:00"
canvas.create_rectangle(10,250,250,360,fill="white",width=2)
canvas.create_text(130,305,text="22:00 - 06:00",font= "Arial 28 bold",fill="black")
canvas.create_line(130,360,130,500,fill="grey",width=20)

#80_02
canvas.create_oval(420,10,660,250,fill="white")
canvas.create_oval(430,20,650,240,fill="red",outline="")
canvas.create_oval(460,50,620,210,fill="white",outline="")
canvas.create_text(540,130,text="80",font= "Arial 80 bold",fill="black")
#Warning_sign_02
canvas.create_rectangle(420,250,660,360,fill="white",width=2)
canvas.create_line(540,360,540,500,fill="grey",width=20)
#CLOUD
canvas.create_rectangle(480,300,600,320,fill="black",outline="")
canvas.create_oval(460,280,500,320,fill="black",outline="")
canvas.create_oval(490,260,570,320,fill="black",outline="")
canvas.create_oval(550,270,600,320,fill="black",outline="")
canvas.create_oval(590,290,620,320,fill="black",outline="")
#RAIN-DROPS
canvas.create_line(470,330,465,340,width=3)
canvas.create_line(480,330,470,350,width=3)

canvas.create_line(490,330,485,340,width=3)
canvas.create_line(500,330,490,350,width=3)

canvas.create_line(510,330,505,340,width=3)
canvas.create_line(520,330,510,350,width=3)

canvas.create_line(530,330,525,340,width=3)
canvas.create_line(540,330,530,350,width=3)

canvas.create_line(550,330,545,340,width=3)
canvas.create_line(560,330,550,350,width=3)

canvas.create_line(570,330,565,340,width=3)
canvas.create_line(580,330,570,350,width=3)

canvas.create_line(590,330,585,340,width=3)
canvas.create_line(600,330,590,350,width=3)

canvas.mainloop()
