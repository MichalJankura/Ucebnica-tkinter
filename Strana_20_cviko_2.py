import tkinter,random
canvas = tkinter.Canvas()
canvas.pack()

x = random.randrange(200)
y = random.randrange(200)
velkost = random.randint(30, 100)
farba = random.choice(('red', 'yellow', 'blue'))
canvas.create_rectangle(x, y, x+velkost, y+velkost, fill=farba)

canvas.create_text(x+(velkost/2), y+(velkost/2), text=velkost,font="Arial 20 bold")


canvas.mainloop()
