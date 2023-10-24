import tkinter
canvas = tkinter.Canvas()
canvas.pack()

#Pre obe elipsy nastavte rôzne farby výplne, obrysov a tiež hrúbky čiar.

canvas.create_oval(100, 50, 200, 100,fill="red",width = 3,outline="yellow")
canvas.create_oval(200, 50, 300, 100,fill="blue",width = 7,outline="pink")

canvas.mainloop()
