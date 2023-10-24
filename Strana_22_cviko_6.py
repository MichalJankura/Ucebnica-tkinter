import tkinter,random
canvas = tkinter.Canvas(width=400,height=400)
canvas.pack()

x = random.randrange(200)
y = random.randrange(200)
size = 150
number = random.choice((30,60,80,40))
canvas.create_oval(x,y,x+size,y+size,fill="red")
canvas.create_oval(x+15,y+15,x+size-15,y+size-15,fill="white")
canvas.create_text(x+size/2,y+size/2,text=number,font="Arial 50 bold")

canvas.mainloop()
