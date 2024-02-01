import tkinter
from random import*
canvas = tkinter.Canvas(width=450, height=450, bg="white")
canvas.pack()

# def pis(event):
#     print(event.keysym)
#     x = randrange(300)
#     y = randrange(300)
#     canvas.create_text(x, y, text=event.keysym)
#
# canvas.bind_all('<Key>', pis)

def pis(event):
    print(f"keysym: {event.keysym}, char: {event.char}, keycode: {event.keycode}")
    x = randrange(300)
    y = randrange(300)
    canvas.create_text(x, y, text=f"keysym: {event.keysym}, char: {event.char}, keycode: {event.keycode}")

canvas.bind_all('<Key>', pis)
canvas.mainloop()
