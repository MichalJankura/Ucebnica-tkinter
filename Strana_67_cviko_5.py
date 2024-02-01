import tkinter
import random
canvas = tkinter.Canvas(width=200, height=400, bg="white")
canvas.pack()

def draw_traffic_light(state):
    canvas.delete("all")
    # Obdlznik semafora
    canvas.create_rectangle(50, 50, 150, 350,fill="black")
    # Rozsvietene svetla
    red = "red" if state in {1, 3, 4} else "black"
    yellow = "yellow" if state in {2, 3, 4} else "black"
    green = "green" if state in {0, 4} else "black"
    # Kresli svetla
    canvas.create_oval(60, 60, 140, 140, fill=red)
    canvas.create_oval(60, 150, 140, 230, fill=yellow)
    canvas.create_oval(60, 240, 140, 320, fill=green)
def change_traffic_light():
    # Vygeneruj novy stav
    state = random.randint(0, 4)
    # Vykresli novy stav
    draw_traffic_light(state)
    # Zavolaj sa znova po 500 ms
    canvas.after(500, change_traffic_light)

change_traffic_light()

canvas.mainloop()