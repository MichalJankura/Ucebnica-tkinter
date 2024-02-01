import tkinter
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()

x = y = 10
ball = canvas.create_oval(x, y, x + 30, y + 30, fill="blue")

def move_ball():
    global x, y
    canvas.move(ball, 5, 5)  # Posunutie lopty o 5 pixelov doprava a 5 pixelov dole
    x += 5  # Update x
    y += 5  # Update y
    if x > 800 or y > 800:  # Podmienka kedy sa resetne lopta
        canvas.move(ball, -x, -y)  # Reset na zaciatok
        x = y = 10  # Reset suradnic
    canvas.after(10, move_ball)  # Animacia sa opakuje kazdych 10 milisekund

move_ball()

canvas.mainloop()