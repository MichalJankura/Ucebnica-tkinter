import tkinter
canvas = tkinter.Canvas(width=800, height=200, bg="white")
canvas.pack()

x = 10
lopta = canvas.create_oval(x, 90, x + 40, 130, fill="blue")

def pohyb_lopty():
    global x
    canvas.move(lopta, 5, 0) # posunutie lopty o 5 pixelov doprava
    x += 5  # posunutie lopty o 5 pixelov doprava updatuje premennu x
    if x < 800:
        canvas.after(20, pohyb_lopty) # opakovanie funkcie pohyb_lopty() po 20 milisekundach

pohyb_lopty()

canvas.mainloop()