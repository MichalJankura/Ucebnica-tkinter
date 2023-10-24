import tkinter,random
canvas = tkinter.Canvas(width=400,height=400)
canvas.pack()

#Vodorovne-zvisle
# for i in range(7):
#     canvas.create_line(10*i, 10, 10*i, 150)
####

#Vodorovne-zvislo shifted
# for i in range(7):
#     canvas.create_line(10*i, 10, 10*i, i*20)
###

#Zviesle shifted
x = 5
for i in range(1,6):
    x = 10+x
    canvas.create_line(x, 55+x, x, 100+x)
###

canvas.mainloop()
