import tkinter
canvas = tkinter.Canvas(width=300, height=200)
canvas.pack()

#---POLAND-FLAG---
canvas.create_rectangle(10, 10, 300, 200, fill='white')
canvas.create_rectangle(10, 10, 300, 100, fill='red')
#-----------------

#---FRANCE-FLAG---
# canvas.create_rectangle(10, 10, 100, 200, fill='blue')
# canvas.create_rectangle(100, 10, 190, 200, fill='white')
# canvas.create_rectangle(190, 10, 280, 200, fill='red')
#-----------------

#---DEUTSCHLAND-FLAG---
# canvas.create_rectangle(0, 10, 300, 60, fill='black')
# canvas.create_rectangle(0, 60, 300, 110, fill='gold')
# canvas.create_rectangle(0, 110, 300, 160, fill='red')
#-----------------

#---HUNGARY-FLAG---
# canvas.create_rectangle(0, 10, 300, 60, fill='red')
# canvas.create_rectangle(0, 60, 300, 110, fill='white')
# canvas.create_rectangle(0, 110, 300, 160, fill='green')
#-----------------

#---SWITZERLAND-FLAG---
# canvas.create_rectangle(0, 0, 300, 200, fill='red')
# canvas.create_line(150,50,150,150,width=40,fill="white")
# canvas.create_line(100,100,200,100,width=40,fill="white")
#-----------------

#---ISRAEL-FLAG---

#-----------------
canvas.mainloop()
