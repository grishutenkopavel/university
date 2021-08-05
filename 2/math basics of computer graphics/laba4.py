from tkinter import *
import math
root = Tk()
root.title('Тело брошенное под углом')
frameV = Frame(root)
frameV.pack()
frameA = Frame(root)
frameA.pack()
frameH = Frame(root)
frameH.pack()

w = 500
h = 500

labelV = Label(frameV, text="V0")
labelV.pack(side = LEFT)
entryV = Entry(frameV)
entryV.pack(side = LEFT)

labelA = Label(frameA, text="a")
labelA.pack(side = LEFT)
entryA = Entry(frameA)
entryA.pack(side = LEFT)

labelH = Label(frameH, text="h")
labelH.pack(side = LEFT)
entryH = Entry(frameH)
entryH.pack(side = LEFT)

def clickOnButton1():
    canv.delete("all")
    v0 = int(entryV.get())
    a = int(entryA.get()) * 3.1415 / 180
    n = int(entryH.get())
    t = 0.1
    g = 9.8
    x0 = 0
    y0 = 0
    x = y = 1
    vx = v0*math.cos(a)
    while x<w and y<h: 
        vy = v0*math.sin(a)-g*t
        x = x0+vx*t/t
        y = y0+(vy*t-g*t*t/2)/t
        xk0 = round(x0)
        xk = round(x)
        yk0 = h - round(y0)-n
        yk = h -round(y)-n
        canv.create_line(xk0,yk0, xk, yk)
        t += 0.1
        x0 = x
        y0 = y
    

button1 = Button(text="OK", command=clickOnButton1)
button1.pack(side = TOP)

canv=Canvas(width=w,height=h,bg="white")
canv.pack(side = BOTTOM)


root.mainloop()