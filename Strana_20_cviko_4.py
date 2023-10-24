import tkinter,random
canvas = tkinter.Canvas()
canvas.pack()

x = random.randrange(250)
y = random.randrange(200)
velkost = 50

canvas.create_line(x,y,x+velkost,y)

#Tento zápis len pre fajnšmekrov len toto nepíš keď máš s MAROŠOM ->
print(f"Začiatok čiary je na x,y[{x},{y}] a koniec x,y[{x+velkost},{y}]")
#TAKTO PÍŠTE VŠETCI (NE)INFORMATICI
print("Začiatok čiary je na x,y[",x,",",y,"] a koniec x,y[",x+velkost,",",y,"]")

canvas.mainloop()
