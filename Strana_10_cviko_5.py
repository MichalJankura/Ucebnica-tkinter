import tkinter
canvas = tkinter.Canvas()
canvas.pack()

#---T---
canvas.create_line(110,10,210,10,width = 2)
canvas.create_line(160,10,160,110,width = 2)
#-------

#---L---
canvas.create_line(110,10,110,110,width = 2)
canvas.create_line(110,110,160,110,width = 2)
#-------

#---H---
canvas.create_line(110,10,110,110,width = 2)
canvas.create_line(110,60,160,60,width = 2)
canvas.create_line(160,10,160,110,width = 2)
#-------

#---T---
canvas.create_line(110,10,210,10,width = 2)
canvas.create_line(210,10,110,110,width = 2)
canvas.create_line(110,110,210,110,width = 2)
#-------

canvas.mainloop()
