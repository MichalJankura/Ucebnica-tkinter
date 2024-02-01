import tkinter
import random

canvas = tkinter.Canvas(width=800, height=200, bg="white")
canvas.pack()

lopta_1 = canvas.create_oval(10, 90, 30, 110, fill="blue")
lopta_2 = canvas.create_oval(770, 90, 790, 110, fill="red")

# Startovne pozicie loptičiek
x1 = 10
x2 = 770

def posun_lopticiek():
    global x1, x2
    # Nasmerovanie loptičiek
    dx1 = random.randint(5, 10)
    dx2 = random.randint(5, 10)
    canvas.move(lopta_1, dx1, 0)
    canvas.move(lopta_2, -dx2, 0)
    x1 += dx1
    x2 -= dx2

    # Podmienka výpisu BUM
    if x1 >= x2:
        canvas.create_text(x1, 100, text="BUM", fill="black", font=("Arial", 30))
    else:
        # Animacia
        canvas.after(10, posun_lopticiek)

posun_lopticiek()
canvas.mainloop()