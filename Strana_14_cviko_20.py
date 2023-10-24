import tkinter
canvas = tkinter.Canvas(bg = 'white', width = 400, height = 400)
canvas.pack()

#globe face
canvas.create_oval(10,10,390,390)

#eyes
canvas.create_oval(80,80,120,120)
canvas.create_oval(280,80,320,120)
#glasses-on-eyes
canvas.create_rectangle(80,80,120,120,width=2)
canvas.create_rectangle(280,80,320,120,width=2)

"""Connection between two eyes """
canvas.create_line(120,100,280,100,width=2)
"""-----------------------------------"""

canvas.create_line(80,100,40,80,width=2)
canvas.create_line(320,100,360,80,width=2)

#nose
canvas.create_rectangle(200,140,220,200)

#mouth
canvas.create_oval(120,310,280,350)

canvas.mainloop()
