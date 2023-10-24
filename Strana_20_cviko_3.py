import tkinter,random
canvas = tkinter.Canvas()
canvas.pack()

x = random.randrange(250)
y = random.randrange(200)
y2 = random.randrange(200)
hrubka = random.randint(2,10)
velkost = random.randint(30, 100)

canvas.create_line(x,y,x+velkost,y2,width=hrubka)

#Tento zápis len pre fajnšmekrov len toto nepíš keď máš s MAROŠOM ->
print(f"Dĺžka čiary je {velkost}px \nHrúbka čiary je {hrubka}px")
#TAKTO PÍŠTE VŠETCI (NE)INFORMATICI
print("Dĺžka čiary je",velkost,"px")
print("Hrúbka čiary je",hrubka,"px")

canvas.mainloop()
