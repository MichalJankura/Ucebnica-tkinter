import tkinter

canvas = tkinter.Canvas(width=100, height=800, bg="white")
canvas.pack()

y = 10
lopta = canvas.create_oval(40, y, 70, y + 30, fill="blue")

def posun_lopty():
    global y
    canvas.move(lopta, 0, 5)  # Posun o 5px dole
    y += 5  # Update y po posune
    if y > 800:  # Podmienka kedy sa resetne lopta
        canvas.move(lopta, 0, -y)  # Move the ball back to the top
        y = 10  # Reštaruj y
    canvas.after(10, posun_lopty)

posun_lopty()
canvas.mainloop()