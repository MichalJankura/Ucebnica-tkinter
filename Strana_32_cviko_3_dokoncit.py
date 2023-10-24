import random
import tkinter
canvas = tkinter.Canvas(width=500,height=500)
canvas.pack()

def tvar(x, y):
    color = random.choice(["red","green","blue"])
    velkost = random.choice([100,150,200])
    canvas.create_rectangle(x,y,x+velkost,y+velkost,fill= color)
    canvas.create_rectangle(x+20,y+10,x+40,y+30,fill="purple")
    canvas.create_rectangle((x+velkost)-20,y+10,(x+velkost)-(velkost/2),y+30,fill="purple")
#
# for i in range(1, 7):
#     vagon(i*120, 100)

tvar(100,100)

canvas.mainloop()
