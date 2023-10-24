import tkinter
canvas = tkinter.Canvas()
canvas.pack()

#DANO S CODE
# canvas.create_rectangle(10,50,110,300, fill='blue', outline='')
# canvas.create_rectangle(60,50,160,300, fill='white', outline='')
# canvas.create_rectangle(110,50,210,300, fill='red', outline='')

#CORRECT CODE
canvas.create_rectangle(10,50,110,300, fill='blue', outline='')
canvas.create_rectangle(110,50,210,300, fill='white', outline='')
canvas.create_rectangle(210,50,310,300, fill='red', outline='')

canvas.mainloop()
