import tkinter
canvas = tkinter.Canvas(width=800 , height = 400)
canvas.pack()
x = 100
y = 100
for i in range(3):
    x=x+150

    #telo
    canvas.create_rectangle(x, y, x+60, y+100, fill='skyblue')
    #hlava
    canvas.create_rectangle(x+10, y-50, x+50, y, fill='skyblue')

    #oci
    canvas.create_rectangle(x+15, y-40, x+25, y-30, fill='yellow')
    canvas.create_rectangle(x+35, y-40, x+45, y-30, fill='yellow')
    #usta
    canvas.create_rectangle(x+15, y-20, x+45, y-10, fill='red')
    #nohy
    canvas.create_rectangle(x, y+100, x+20, y+180, fill='skyblue')
    canvas.create_rectangle(x+40, y+100, x+60, y+180, fill='skyblue')
    #ruky
    canvas.create_line(x, y+10, x-40, y+50, width=15)
    canvas.create_line(x+60, y+10, x+110, y+50, width=15)


canvas.mainloop()
