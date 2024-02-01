import tkinter
import random
canvas = tkinter.Canvas(width=600, height=600, bg="white")
canvas.pack()

def farba():
    farba = random.choice(["red", "green", "blue", "yellow", "cyan", "magenta", "skyblue", "pink", "orange", "purple",
                           "black", "white", "grey", "brown", "violet", "turquoise", "gold", "silver", "navyblue",])
    return farba

def obrazok_1():
    for i in range(150):
        hrubka = random.randrange(7, 10)
        y1 = random.randrange(0, 600)
        y2 = random.randrange(0, 600)
        canvas.create_line(0, y1, 600, y2, fill=farba(),width=hrubka)

def obrazok_2():
    for i in range(150):
        hrubka = random.randrange(7, 10)
        x1 = random.randrange(0, 600)
        x2 = random.randrange(0, 600)
        canvas.create_line(x1, 0, x2, 600, fill=farba(),width=hrubka)

def obrazok_3():
    x = 300
    y = 300
    for i in range(150):
        hrubka = random.randrange(7, 10)
        x1 = random.randrange(0, 600)
        y1 = random.randrange(0, 600)
        canvas.create_line(x, y, x1, y1, fill=farba(),width=hrubka)

obrazok_3()
#obrazok_2()
#obrazok_1()
canvas.mainloop()