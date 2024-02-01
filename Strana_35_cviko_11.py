import tkinter
import random

# Create a canvas
canvas = tkinter.Canvas(width=1900, height=500, bg="white")
canvas.pack()
#20 kruhov
for i in range(20):
    x = 50 + i * 90
    # Farba kruhu
    color = random.choice(["red", "green", "blue", "yellow", "cyan", "magenta", "skyblue", "pink", "orange", "purple"])
    # Velkost kruhu
    radius = random.randrange(50, 100)
    # Draw the circle
    canvas.create_oval(x - radius, 250 - radius, x + radius, 250 + radius, outline=color, width=3)

canvas.mainloop()