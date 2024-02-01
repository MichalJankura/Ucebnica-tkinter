import tkinter
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()

# STREDNA CIARA
canvas.create_line(0, 400, 800, 400)

def kresli_tvar(suradnice):
    if suradnice.y < 400:
        canvas.create_rectangle(suradnice.x - 20, suradnice.y - 20, suradnice.x + 20, suradnice.y + 20, fill="blue")
    else:
        canvas.create_oval(suradnice.x - 20, suradnice.y - 20, suradnice.x + 20, suradnice.y + 20, fill="yellow")

canvas.bind("<Button-1>", kresli_tvar)
canvas.mainloop()

"Strana_44_cviko_2"
"""Áno, program bude stále fungovať aj bez časti else v príkaze if,
 ale bude sa správať inak. Konkrétne, kreslí len modrý štvorec, 
 keď kliknete nad čiaru. Ak kliknete pod čiaru, nekreslí nič, 
 pretože tam nie je žiadna časť else, ktorá by tento prípad riešila."""