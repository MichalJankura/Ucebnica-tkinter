import tkinter
canvas = tkinter.Canvas()
canvas.pack()

#K elipse canvas.create_oval(100, 50, 200, 100)
# nakreslite tesne vedľa nej rovnako veľkú elipsu.

canvas.create_oval(100, 50, 200, 100)
canvas.create_oval(200, 50, 300, 100)

canvas.mainloop()
