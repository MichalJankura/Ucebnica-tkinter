import tkinter,random
canvas = tkinter.Canvas(width=400,height=400)
canvas.pack()

#Skúste odhadnúť, čo nakreslí nasledujúci program:
x = 0
for i in range(1,11):
    x = x+20
    canvas.create_rectangle(x, 10, x+10, 20)
"""
Experimentujte s číslami v programe a zistite, ako zmenia nakreslený obrázok a pozorovanie
zdôvodnite.
Čo sa stane, ak v riadku x = 0 zadáme iné číslo? Odpoveď : 1. obdlznik sa kresli na osi x dalej
Čo sa stane, ak v riadku x = x+20 zadáme namiesto 20 iné číslo? Odpoveď : Rozostup medzi obdlznikmy bude väčší
Čo sa stane, ak v príkaze rectangle zmeníme 15 na iné číslo? Odpoveď : Zmeníme tvar a veľkosť. (10 --> [])
"""
canvas.mainloop()
