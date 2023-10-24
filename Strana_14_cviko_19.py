import tkinter
canvas = tkinter.Canvas(bg = 'white', width = 400, height = 400)
canvas.pack()

#globe face
canvas.create_oval(10,10,390,390)

#eyes
canvas.create_oval(80,80,120,120)
canvas.create_oval(280,80,320,120)

#nose
canvas.create_rectangle(200,140,220,200)

#mouth
canvas.create_oval(120,310,280,350)

canvas.mainloop()
