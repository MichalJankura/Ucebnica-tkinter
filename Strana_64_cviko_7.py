import tkinter
from random import *
canvas = tkinter.Canvas()
canvas.pack()

def kresli_lopticku(x, y):
    canvas.create_oval(x-5, y-5,x+5, y+5, fill='red')

def kresli_kurzor(x, y):
    width = max(50 - pocet_bodov, 10)  # Decrease the width of the cursor as the number of points increases
    canvas.create_line(x, y, x+width, y, fill='blue', width=5)

def vypis_body(pocet_bodov):
    canvas.create_text(100, 10, text='Počet získaných bodov:')
    canvas.create_text(200, 10, text=pocet_bodov)

def draw_smiley_face(x, y):
    # Draw a circle for the face
    canvas.create_oval(x-50, y-50, x+50, y+50, fill='yellow')
    # Draw two circles for the eyes
    canvas.create_oval(x-20, y-20, x-10, y-10, fill='black')
    canvas.create_oval(x+20, y-20, x+10, y-10, fill='black')
    # Draw an arc for the mouth
    canvas.create_arc(x-30, y-10, x+30, y+20, start=0, extent=-180, fill='black')

def timer1():
    canvas.delete('all')
    global lopticka_x, lopticka_y, pocet_bodov
    speed = min(pocet_bodov + 5, 20)  # Increase the speed of the falling ball as the number of points increases
    lopticka_y = lopticka_y + speed
    kresli_lopticku(lopticka_x, lopticka_y)
    kresli_kurzor(kurzor_x, kurzor_y)
    vypis_body(pocet_bodov)
    if kurzor_x<lopticka_x<kurzor_x+50 and kurzor_y-10<lopticka_y<kurzor_y:
        pocet_bodov = pocet_bodov + 1
        lopticka_x = randrange(300)
        lopticka_y = 20
    elif lopticka_y>300:
        pocet_bodov = pocet_bodov - 1  # Subtract a point if the ball has reached the bottom
        lopticka_x = randrange(300)
        lopticka_y = 20
    if pocet_bodov >= 5:  # If the number of points is greater than or equal to 20
        print("Gratulujem k úspechu!")  # Print a congratulatory message
        draw_smiley_face(400, 400)  # Draw a happy smiley face
        return
    canvas.after(10, timer1)

def posun_mysi(suradnice):
    global pocet_bodov, kurzor_x
    kurzor_x = suradnice.x
    canvas.delete('all')
    kresli_lopticku(lopticka_x, lopticka_y)
    kresli_kurzor(kurzor_x, kurzor_y)
    vypis_body(pocet_bodov)

pocet_bodov = 0
lopticka_x = randrange(300)
lopticka_y = 20
kurzor_x = 150
kurzor_y = 250

timer1()
canvas.bind('<Motion>', posun_mysi)

canvas.mainloop()