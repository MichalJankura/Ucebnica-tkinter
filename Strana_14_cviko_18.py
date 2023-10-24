import tkinter
canvas = tkinter.Canvas(bg = 'white', width = 400, height = 400)
canvas.pack()




canvas.create_oval(120,20,220,120)
canvas.create_oval(150,90,190,110)

canvas.create_line(160,120,100,150)
canvas.create_line(100,100,100,250)
canvas.create_line(100,150,80,100)
canvas.create_line(100,150,120,100)
canvas.create_line(180,120,240,140)
canvas.create_oval(145,60,150,65,fill="black")
canvas.create_oval(165,60,170,65,fill="black")
canvas.create_oval(165,170,170,175,fill="black")
canvas.create_oval(165,270,170,275,fill="black")
canvas.create_oval(120,120,220,220)
canvas.create_oval(120,220,220,320)

# x1,y1 = 200,100
# x2,y2= 200,200
# x3,y3 = 200,300
# r = 50
#
# canvas.create_oval(x1 - r, y1 - r, x1 + r, y1 + r, fill="white", outline="black")
# canvas.create_oval(x2 - r, y2 - r, x2 + r, y2 + r, fill="white", outline="black")
# canvas.create_oval(x3 - r, y3 - r, x3 + r, y3 + r, fill="white", outline="black")


canvas.mainloop()
