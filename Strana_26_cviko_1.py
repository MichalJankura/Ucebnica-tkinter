import tkinter,random
canvas = tkinter.Canvas(width=400,height=400)
canvas.pack()

#Vodorovne
# for i in range(7):
#     canvas.create_line(10, i*10, 200, i*10)
####

#Vodorovne shifted
# for i in range(7):
#     canvas.create_line(10*i, i*10, 200, i*10)
###

#Nahnute
for i in range(7):
    canvas.create_line(10, i*10, 200, i*20)
###

canvas.mainloop()
