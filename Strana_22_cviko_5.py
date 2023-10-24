import tkinter,random
canvas = tkinter.Canvas()
canvas.pack()

x=100
y=100

canvas.create_rectangle(100, 100, 160, 200, fill='skyblue') #telo
canvas.create_rectangle(110, 50, 150, 100, fill='skyblue') #hlava
#oci
canvas.create_rectangle(115, 60, 125, 70, fill='yellow')
canvas.create_rectangle(135, 60, 145, 70, fill='yellow')
canvas.create_rectangle(115, 80, 145, 90, fill='red') #usta
#nohy

canvas.create_rectangle(100, 200, 120, 280, fill='skyblue')
canvas.create_rectangle(140, 200, 160, 280, fill='skyblue')
#ruky
canvas.create_line(100,110,60,150, width=15)
canvas.create_line(160,110,210,150, width=15)

#antena
canvas.create_line(130, 30, 130, 50)

#usi
canvas.create_oval(x, y-30, x+10, y-20, fill="skyblue")
canvas.create_oval(x+50, y-30, x+60, y-20, fill="skyblue")

#meno
canvas.create_text(x+30, y+50, text="FERKO",font="Arial 10")

canvas.mainloop()
