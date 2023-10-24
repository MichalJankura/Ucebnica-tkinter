import tkinter
canvas = tkinter.Canvas(width=400,height=400)
canvas.pack()

"""
Skúste vymyslieť iný zápis programu, ktorý nakreslí rovnaký obrázok ako tento program:
x = 0
for i in range(1,11):
    x = x + 20
    canvas.create_rectangle(x, 10, x+15, 20)
"""

#SOLUTION
for i in range(1,11):
    x = 20*i
    canvas.create_rectangle(x, 10, x+15, 20)
###

canvas.mainloop()
