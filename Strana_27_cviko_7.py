import tkinter
canvas = tkinter.Canvas(width=800,height=400)
canvas.pack()
for i in range(3):
    canvas.create_text(400,200,text="ŤAHAŤ",font="Arial 70",angle = i*60,fill="blue")

canvas.mainloop()
