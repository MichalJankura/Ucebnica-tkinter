import tkinter
import random
canvas = tkinter.Canvas(width=600, height=600, bg="white")
canvas.pack()

def farba():
    farba = random.choice(["red", "green", "blue", "yellow", "cyan", "magenta", "skyblue", "pink", "orange", "purple"])
    return farba

def baloniky():
    for i in range(8):
        x = 10 + i * 70
        farby=farba()
        canvas.create_oval(x, 10, x + 100, 110, fill=farby, outline="")  # Size of balloon is 100
        canvas.create_line(x + 50, 110, 300,600)  # Draw a line from the bottom of the balloon to the point (300, 600)

def kolotoc():
    for i in range(8):
        x = 10 + i * 70
        farby=farba()
        canvas.create_oval(x, 490, x + 100, 590, fill=farby, outline="")
        canvas.create_line(x + 50, 490, 300, 0)

#baloniky()
kolotoc()

canvas.mainloop()