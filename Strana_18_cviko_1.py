import tkinter,random
canvas = tkinter.Canvas()
canvas.pack()


number = random.randint(1,49)

canvas.create_text(20,20,text=number,font= "Arial 15 bold")
canvas.create_text(50,20,text=number,font= "Arial 15 bold")
canvas.create_text(80,20,text=number,font= "Arial 15 bold")
canvas.create_text(120,20,text=number,font= "Arial 15 bold")
canvas.create_text(150,20,text=number,font= "Arial 15 bold")
canvas.create_text(180,20,text=number,font= "Arial 15 bold")
canvas.create_text(210,20,text=number,font= "Arial 15 bold")

#QUESTION
"""Myslíte si, že môžeme takýto
program použiť na žrebovanie čísel v lotérii? Svoju odpoveď zdôvodnite."""

#ANSWER
"""Tento program nemožno použiť pre losovanie 6ich náhodných čísel pretože 
program vygeneruje náhodné číslo len raz"""

#FIX-ODPOVED ZA + ABO 1

"""Pomocou cyklu for vygenerujeme 6 náhodných čisel , ktoré si uložíme do zoznamu
Pomocou ďalšieho cyklu budeme prechádzať uložené čísla v zozname
Cyklus taktiež využijeme na vypisovanie čísel do pola"""

"""Alebo použijeme dvojitý cyklus teda cyklus v cykle prvý cyklus nám vygeneruje
prve cislo a druhý cyklus nám ho vypíše na plátno pričom os x sa bude posúvať"""
canvas.mainloop()

