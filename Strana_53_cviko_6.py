import tkinter
import random

canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()

x = y = 10
pocet_0 = pocet_1 = 0
paused = False

def pis_cisla():
    global x, y, pocet_0, pocet_1, paused
    if not paused:
        # Generátor (0 or 1)
        num = random.randint(0, 1)

        # Piš číslo na canvas
        color = "blue" \
            if num == 0 \
            else "green"
        canvas.create_text(x, y, text=str(num), fill=color)

        # Update the count of zeros and ones
        if num == 0:
            pocet_0 += 1
        else:
            pocet_1 += 1

        # Update the position for the next number
        x += 20
        if x > 800:
            x = 10
            y += 20

        # Ak sa dostaneme na koniec canvasu, vypíšeme počet 0 a 1 do shellu
        if y > 800:
            print(f"Počet 0iek: {pocet_0}")
            print(f"počet 1iek: {pocet_1}")
        else:
            # Call this function again after 100 milliseconds
            canvas.after(10, pis_cisla)

def pause_resume(event):
    global paused
    paused = not paused
    if not paused:
        pis_cisla()

# Po stlačení klávesy 'p' sa program pozastaví alebo pokračuje
canvas.bind_all('p', pause_resume)
pis_cisla()

canvas.mainloop()