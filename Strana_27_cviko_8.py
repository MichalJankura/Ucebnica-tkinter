import tkinter
canvas = tkinter.Canvas(width=800,height=400)
canvas.pack()

"""TOTO JE UPLNÝ !PODS! VEDIA LEN OG CGSMACI NA INF """
"""Keď nedáte dostatok <space> pred slovo tak nikdy nedosiahnete daný výsledok
tajomstvo úspechu je proste medzera"""
for i in range(6):
    canvas.create_text(400,200,text="               Python",font="Arial 20",angle = i*60,fill="black")

canvas.mainloop()
