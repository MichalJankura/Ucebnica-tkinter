import tkinter
canvas = tkinter.Canvas(width=800, height=900)
canvas.pack()

def draw_tree_with_cherry(x, y):
    #KOREN
    canvas.create_line(x+100,y+190,x+100,y+400,fill="black",width=50)
    # KORUNA
    canvas.create_oval(x,y,x+200,y+200, fill='green', outline='')
    #CERESNE
    canvas.create_oval(x+100,y+100,x+125,y+125,fill="red")
    canvas.create_oval(x + 60, y + 100, x + 85, y + 125, fill="red")
    #STOPKY CERESNI
    canvas.create_line(x+75,y+100,x+90,y+70,width=5)
    canvas.create_line(x+90,y+70,x+110,y+100,width=5)

draw_tree_with_cherry(400,250)
canvas.mainloop()
