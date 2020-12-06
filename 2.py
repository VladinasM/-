from tkinter import *
import time
root = Tk()
 
canvas = Canvas(root, bg='white', height=800, width=800)
canvas.pack()
 
a = canvas.create_oval((500, 371), (537, 408), fill='black')
b = canvas.create_oval((214, 371), (251, 408), fill='red')
c = canvas.create_rectangle((502, 374), (529, 400), fill='blue')
def move():
    k1 = 500 - 214
    kx = -1
    for i in range(33):
        canvas.move(c,0.03*k1*kx, 0)
        canvas.update()
        time.sleep(0.03)
 
B = Button(root, text ="Движение к красному", command = move)
 
B.pack()
 
root.mainloop()
