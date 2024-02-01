import tkinter
canvas = tkinter.Canvas(width=800, height=900)
canvas.pack()

def ballon_with_basket(x, y):
    #Balonik
    canvas.create_oval(x + 50, y + 50, x + 250, y + 250, fill="blue")
    #Lana
    canvas.create_line(x+50,y+160,x+150,y+500)
    canvas.create_line(x+250,y+160,x+150,y+500)
    #Kosik
    canvas.create_rectangle(x+100,y+500,x+200,y+550,fill="red")

ballon_with_basket(150,40)
canvas.mainloop()