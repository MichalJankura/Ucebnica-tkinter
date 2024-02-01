import tkinter
import random
canvas = tkinter.Canvas(width=1080, height=800, bg="white")
canvas.pack()


def ostrov():
    canvas.create_oval(50, 350, 300, 450,fill="#8a710f", outline="")
    #Stožiar
    canvas.create_line(170, 350, 170, 150, fill="black", width=5)
    #Vlajka
    canvas.create_rectangle(170, 10, 370, 150, fill="green",width=5)
    #Mesiac
    canvas.create_oval(210, 30, 310, 130, fill="yellow", outline="")
    canvas.create_oval(250, 30, 320, 130, fill="green", outline="")
def voda():
    canvas.create_rectangle(0, 400, 1080, 800, fill="blue", outline="")

def lodka():
    canvas.create_line(450, 420, 650, 420, fill="black", width=5)  # Spodok
    canvas.create_line(450, 420, 410, 350, fill="black", width=5)  # Lavo-bok
    canvas.create_line(650, 420, 690, 350, fill="black", width=5)  # Pravo-bok
    canvas.create_line(410, 350, 690, 350, fill="black", width=5)  # Vrch
    #Stožiar
    canvas.create_line(550, 350, 550, 100, fill="black", width=5)
    #Vlajka
    canvas.create_line(550,100,600,250,fill="black",width=5)
    canvas.create_line(600, 250, 550, 320, fill="black", width=5)

def mesiac():
    canvas.create_oval(800, 100, 1000, 300, fill="yellow", outline="")
    canvas.create_oval(870, 100, 1020, 300, fill="white", outline="")
    #Odraz mesiaca vo vode
    canvas.create_oval(800, 500, 1000, 700, fill="yellow", outline="")
    canvas.create_oval(870, 500, 1020, 700, fill="blue", outline="")



ostrov()
voda()
mesiac()
lodka()

canvas.mainloop()