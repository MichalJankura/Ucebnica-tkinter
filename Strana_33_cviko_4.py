import tkinter
import random
canvas = tkinter.Canvas(width=600, height=600, bg="white")
canvas.pack()

def ciarovy_kod():
    pocet_ciar = 20
    for i in range(pocet_ciar):
        hrubka = random.randint(8, 15)
        pozicia_ciary = (i + 1) * pocet_ciar
        # Čiary
        canvas.create_line(pozicia_ciary, 10, pozicia_ciary, 600, width=hrubka)
        # Výpis
        print("HRUBKA čiary: ", i ,"je: ", hrubka)
ciarovy_kod()
canvas.mainloop()